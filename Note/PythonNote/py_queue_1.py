import threading
import time 
import queue

def product(qu):
    str_tuple = ('name','age','sex')
    for i in range(99999):
        print(threading.current_thread(). name + 'product for tuple')
        time.sleep(0.2)
        qu.put(str_tuple[i % 3])
        print(threading.current_thread(). name + 'product env is ok')

def consume(qu):
    while True:
        print(threading.current_thread(). name + 'consume for tuple')
        time.sleep(0.2)
        t = qu.get()
        print(threading.current_thread().name + 'Consume %s is ok'  % t)

qu = queue.Queue(maxsize=1)

threading.Thread(target=product,args=(qu,)).start()
threading.Thread(target=product,args=(qu,)).start()
threading.Thread(target=product,args=(qu,)).start()

threading.Thread(target=consume,args=(qu,)).start()

