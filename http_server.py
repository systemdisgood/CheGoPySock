import threading
import socket

def print_thread_func(argument):
    while 1:
        print(argument)

print_thread1 = threading.Thread(target=print_thread_func, name="print_thread", args=("heh",))
print_thread1.start()

print_thread2 = threading.Thread(target=print_thread_func, name="print_thread", args=("hoh",))
print_thread2.start()

print_thread1.join()
print_thread2.join()