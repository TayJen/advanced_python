from concurrent.futures import as_completed, Executor, ProcessPoolExecutor, ThreadPoolExecutor, wait
import math
import time


def save_results(exec_name: str, n_jobs: int, time: float):
    with open('./artifacts/4_2_result.txt', 'a+') as f:
        f.write(f"{exec_name} with {n_jobs} n_jobs time: {time:.3f}\n")


def add_range_integral(f, a, step, i_start, i_end):
    res = 0
    for i in range(i_start, i_end):
        res += f(a + i * step) * step
    return res


def integrate(f, a, b, executor_type: str, n_jobs: int = 1, n_iter: int = 50000000):
    if executor_type == 'ProcessPoolExecutor':
        executor = ProcessPoolExecutor(n_jobs)
    elif executor_type == 'ThreadPoolExecutor':
        executor = ThreadPoolExecutor(n_jobs)
    else:
        return 0

    acc = 0
    step = (b - a) / n_iter

    with open('./artifacts/4_2_log.txt', 'a+') as f_log:
        f_log.write(f"{executor_type} with {n_jobs} jobs is started at {time.time() % 10000}\n")

    start_time = time.time()
    futures = []
    for i in range(n_jobs):
        pool_range = math.ceil(n_iter / n_jobs)
        i_start = i * pool_range
        i_end = min(n_iter, i_start + pool_range)
        futures.append(executor.submit(add_range_integral, f, a, step, i_start, i_end))

    acc = sum([f.result() for f in futures])
    end_time = time.time()
    save_results(executor_type, n_jobs, end_time - start_time)

    with open('./artifacts/4_2_log.txt', 'a+') as f_log:
        f_log.write(f"{executor_type} with {n_jobs} jobs is finished! Answer: {acc:.3f}, time working: {end_time - start_time}\n\n")

    return acc


if __name__ == "__main__":
    for n_jobs in range(1, 9):
        integrate(math.cos, 0, math.pi / 2, 'ThreadPoolExecutor', n_jobs)
    with open('./artifacts/4_2_result.txt', 'a+') as f:
        f.write('\n\n')
    for n_jobs in range(1, 9):
        integrate(math.cos, 0, math.pi / 2, 'ProcessPoolExecutor', n_jobs)
