import multiprocessing
import time
import threading


N = 200000

def fib(n: int) -> int:
    if n == 0:
        return 0

    a0, a1 = 0, 1
    for _ in range(n-1):
        a0, a1 = a1, a0 + a1

    return a1


def save_results(exp_name: str, time: float):
    with open('./artifacts/4_1_result.txt', 'a+') as f:
        f.write(f"{exp_name} time: {time:.3f}\n")


def calc_time_and_sive(exp_name: str):
    def decorator(f):
        def wrapper(*args, **kwargs):
            start_time: float = time.time()
            res = f(*args, **kwargs)
            end_time: float = time.time()
            save_results(exp_name, end_time - start_time)
            return res
        return wrapper
    return decorator


@calc_time_and_sive('Synchronous')
def synchronous():
    for _ in range(10):
        for _ in range(10):
            fib(N)


@calc_time_and_sive('Multithreading')
def multi_thread():
    threads = []
    for _ in range(10):
        for _ in range(10):
            thread = threading.Thread(target=fib, args=(N,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


@calc_time_and_sive('Multiprocessing')
def multi_process():
    processes = []
    for _ in range(10):
        for _ in range(10):
            process = multiprocessing.Process(target=fib, args=(N,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


if __name__ == "__main__":
    synchronous()
    multi_thread()
    multi_process()
