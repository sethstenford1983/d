import time
import random
import threading




def api(result):
    time.sleep(1)
    result['j'] = random.randint(1,100)


def fn1():
    a = {}
    st = time.time()
    for i in range(5):
        api(a)
    return time.time() - st
#print(fn1())

def experiment():
    threads = []
    for _ in range(3):
        result = {}
        t = threading.Thread(target=api, args=(result, ))
        t.start()
        threads.append([t, result])
    thread_number = 1
    for thread, r in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(r['j']))
        thread_number = thread_number + 1
experiment()