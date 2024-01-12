# 1. Creating and running threads
from multithreading import Thread
import time

#
# def square_numbers():
#     for i in range(100):
#         i * i
#
#
# if __name__ == "__main__":
#     threads = []
#     num_threads = 10
#
#     #create threads
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
#
#     #start threads
#     for thread in threads:
#         thread.start()
#
#     #join threads, wait for them to complete
#     for thread in threads:
#         thread.join()
#
#     print("end")

# 2. share data between threads
# database_value = 0


# def increase():
#     global database_value
#     local_copy = database_value
#     local_copy += 1
#     time.sleep(0.1)
#     database_value = local_copy
#
#
# if __name__ == "__main__":
#     print('start_value', database_value)
#
#     thread1 = Thread(target=increase)
#     thread2 = Thread(target=increase)
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#     print('end value', database_value)
#     print("end")

# 3. Using Locks
# from threading import Lock
#
# database_value = 0
#
#
# def increase(lock):
#     global database_value
#
#     # using lock as a context manager to safely lock and unlock
#     with lock: # in this case we don't have to write lock acquire and lock release
#         # lock.acquire()  # lock the state
#         local_cpy = database_value
#         local_cpy += 1
#         time.sleep(0.1)
#         database_value = local_cpy
#         # lock.release()  # unlock the state
#
#
# if __name__ == "__main__":
#     lock = Lock()
#     print('start value', database_value)
#
#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#     print("end value", database_value)
#     print("end main")

# Queue- FIFO
# from queue import Queue
#
# # create queue
# q = Queue()
#
# # add elements
# q.put(1)
# q.put(2)
# q.put(3)
#
# # now q looks like this:
# # back --> 3 2 1 --> front
# first = q.get()  # Remove and return the first item.
# print(first)
# # now q looks like this:
# # back --> 3 2 --> front

# Use of Queue in Multi Threading
from multithreading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name},got {value}')
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # background threads that automatically die when the main program ends.
        thread.start()

    for i in range(1, 20):
        q.put(i)

    q.join()
    print("end main")
