import concurrent.futures
import time
import random


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


def counter():
    c = 0
    while True:
        yield c
        c += 1


c = counter()


def stall_cpu(operations):
    ret = ''
    for _ in range(operations):
        ret += f'{hash(random.random())}\t#{next(c)}\n'
    return ret


def multithread():

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    # old way of doing threads, but good to know as a fundamental
    # threads = []

    # for _ in range(10):
    #     t = threading.Thread(target=do_something, args=[1.5])
    #     t.start()
    #     threads.append(t)

    # for thread in threads:
    #     thread.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


def multiprocess():

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = []
        for _ in range(6):
            results.append(executor.submit(stall_cpu, 5000))

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


def singleprocess():
    start = time.perf_counter()

    for _ in range(60):
        print(stall_cpu(2000))

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


if __name__ == '__main__':
    # multithread()
    multiprocess()
    time.sleep(5)
    singleprocess()
