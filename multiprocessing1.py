import time
from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os


# 1. create and run processes
# def square_numbers():
#     for i in range(100):
#         i * i
#
#
# if __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count()  # number of CPUs on the machine. Usually a good choice for the number of processes
#
#     # create a process and assign function to each process
#     process = Process(target=square_numbers)
#     processes.append(process)
#
#     # start all processes
#     for process in processes:
#         process.start()
#
#     # wait for all processes to finish
#     # block the main program until these processes are finished
#     for process in processes:
#         process.join()

# 2. share data between processes and use locks
# def add100(number, lock):
#     for i in range(100):
#         time.sleep(0.1)
#         with lock:  # lock as a context manager
#             # lock.acquire()
#             number.value += 1
#         # lock.release()
#
#
# def add_100_array(numbers, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             lock.acquire()
#             numbers[i] += 1
#             lock.release()
#
#
# if __name__ == "__main__":
#     lock = Lock()
#     shared_num = Value('i', 0)
#     print("Number at beginning is", shared_num.value)
#
#     shared_array = Array('d', [0.0, 100.0, 200.0])
#     print('Array at beginning:', shared_array[:])
#
#     p1 = Process(target=add100, args=(shared_num, lock))
#     p2 = Process(target=add100, args=(shared_num, lock))
#
#     p3 = Process(target=add_100_array, args=(shared_array, lock))
#     p4 = Process(target=add_100_array, args=(shared_array, lock))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#
#     print("Number at the end is", shared_num.value)
#     print('Array at end:', shared_array[:])


# 3. using queue in multiprocessing
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i * i)
#
#
# def negative(numbers, queue):
#     for i in numbers:
#         queue.put(i * -1)
#
#
# if __name__ == "__main__":
#     numbers = range(1, 6)
#     q = Queue()
#
#     p1 = Process(target=square,args=(numbers,q))
#     p2 = Process(target=negative,args=(numbers,q))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     while not q.empty():
#         print(q.get())

# 4. Process pools
def cube(number):
    return number * number * number


if __name__ == "__main__":
    numbers = range(10)

    p = Pool()

    result = p.map(cube, numbers)

    p.close()
    p.join()

    print(result)
