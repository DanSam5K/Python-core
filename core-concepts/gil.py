# Stands for Global Interpreter Lock
# Helps sync access to python objects and prevent multiple thread frome executing bytecodes simultaneously
# GIL ensures that only on thread excutes python bytecode at a time even on multi-core systems

# Why is GIL considered good?
# - Simplified MM:
   # -- by elimininating need for thread-safe m-alloc and m-dealloc, makes debugging easier
# - Thread safety for CPython:
   # -- allow multithread to exec python code without worrying about low-level locking and sync
# - Protecting Python Objects:
  # -- Since manage by GIL provide protection against races and ensure integrity od internal data structures

# Why is GIL often considered bad?
# - Limited multi core Perf:
    # --prevent multiple threads from exec python bytecode in parallel,
    # --CPU perf bond task is limited
# - Impacts concurrent I/O-bound workloads
   # if high degree of parallelism is required it can be affected
# - Hinders CPU-Intensive multithreading:
  # -- Alternatives approaches like multiprocessing or Using non-CPython implementations like Jython pr IronPython

import threading

counter = 0

def increment():
    global counter
    for _ in range(10000000):
        counter +=1
        
def decrement():
    global counter
    for _ in range(10000000):
        counter -=1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)