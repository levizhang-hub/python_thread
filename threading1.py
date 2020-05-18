#encoding:utf-8
import threading
from queue import Queue
import copy
import time
def job(l,q):
    total=sum(l)
    q.put(total)
    
def normal(l):
    total=sum(l)
    return total
    
def main(l):
    q=Queue()
    threads=[]
    for i in range(4):
        t=threading.Thread(target=job,args=(copy.copy(l),q))
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)
if __name__ =='__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ', time.time()-s_t)
    s_t = time.time()
    main(l)
    print('multithreading: ', time.time()-s_t)