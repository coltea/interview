import threading


def target_a(counter=10):
    while counter:
        locka.acquire()  # 获取对方的锁，释放自己的锁
        print('a', end='')
        lockb.release()
        counter -= 1


def target_b(counter=10):
    while counter:
        lockb.acquire()
        print('b', end='')
        lockc.release()
        counter -= 1


def target_c(counter=10):
    while counter:
        lockc.acquire()
        print('c\n', end='')
        locka.release()
        counter -= 1


if __name__ == '__main__':
    lock_a = threading.Lock()  # 定义3个互斥锁
    lock_b = threading.Lock()
    lock_c = threading.Lock()

    lockb.acquire()
    lockc.acquire()

    t1 = threading.Thread(target=target_a)  # 定义3个线程
    t2 = threading.Thread(target=target_b)
    t3 = threading.Thread(target=target_c)

    t1.start()
    t2.start()
    t3.start()
