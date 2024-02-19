import multiprocessing
import time
t1=time.time()
l1=[1,2,3]
def time1():
    time.sleep(2)
    l1.append(0)
    print("time1",l1)
def time2():
    time.sleep(2)
    print("time2")
with multiprocessing.Manager() as manager:
    l1=manager.list(l1)
    p1=multiprocessing.Process(target=time1)
    p2=multiprocessing.Process(target=time2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(l1)
    t2=time.time()
    print((t2-t1))

        