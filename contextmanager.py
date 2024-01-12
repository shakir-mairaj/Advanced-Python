# Context manager uses
# 1. Open and close files
# with open("word_list.txt", 'w') as file:
#     file.write("hat")


# 2. Use as a lock
# from threading import Lock
# with lock:

# Implementing context manager as class and handling exceptions
# class ManagedFile:
#     def __init__(self, filename):
#         print('init')
#         self.filename = filename
#
#     def __enter__(self):
#         print("enter")
#         self.file = open(self.filename, 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#         print("exit")
#
#
# with ManagedFile('notes.txt') as f:
#     print("manage file")
#     f.write("context manager")

# context manager as generator
from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')

    try:
        yield f

    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('context manager as generator')
