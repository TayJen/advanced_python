import codecs
import multiprocessing as mp
import time
import queue


class MainProcess():
    def __init__(self, filename_stdin, filename_stdout):
        self.queue_to_a = mp.Queue()
        self.queue_to_b = mp.Queue()
        self.filename_stdin = filename_stdin
        self.filename_stdout = filename_stdout
    
    def send(self, lock):
        with open(self.filename_stdin, 'r') as f_stdin:
            lines = f_stdin.readlines()
            for line in lines:
                msg = line.strip('\n')
                self.queue_to_a.put(msg)
                with lock:
                    with open(self.filename_stdout, 'a') as f_stdout:
                        f_stdout.write(f"Got stdin message: {msg} at {time.time() % 1000}\n")
    
    def recv(self, lock):
        while True:
            try:
                res = self.queue_to_b.get()
                with lock:
                    with open(self.filename_stdout, 'a') as f_stdout:
                        f_stdout.write(f"Got result message: {res} at {time.time() % 1000}\n")
                    print(res)
            except queue.Empty:
                print("Main Process ain't got nothing yet")


class ProcessA():
    def __init__(self, main_process: MainProcess, pipe_entry):
        self.main = main_process
        self.pipe = pipe_entry

    def send(self, msg: str):
        self.pipe.send(msg.lower())
        time.sleep(5)

    def recv(self):
        while True:
            try:
                msg = self.main.queue_to_a.get()
                self.send(msg)
            except queue.Empty:
                print("A_Process ain't got nothing yet")


class ProcessB():
    def __init__(self, main_process: MainProcess, pipe_out):
        self.main = main_process
        self.pipe = pipe_out

    def send(self, msg: str):
        self.main.queue_to_b.put([msg])

    def recv(self):
        while True:
            msg = self.pipe.recv()
            print(f"B_Process got message {msg}")
            if msg:
                self.send(codecs.encode(msg, 'rot_13'))


if __name__ == '__main__':
    filename_stdin = "./artifacts/4_3_stdin.txt"
    filename_stdout = "./artifacts/4_3_stdout.txt"
    
    a, b = mp.Pipe(duplex=False)
    lock = mp.Lock()
    
    main = MainProcess(filename_stdin, filename_stdout)
    A = ProcessA(main, b)
    B = ProcessB(main, a)
    
    x1 = mp.Process(target=main.recv, args=(lock,))
    x2 = mp.Process(target=B.recv, args=())
    x3 = mp.Process(target=A.recv, args=())
    
    for x in x1, x2, x3:
        x.start()
    
    main.send(lock)
