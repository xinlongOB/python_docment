# 使用互斥锁解决资源竞争
# 定义一个全局变量
import time
import threading

num = 0


def test1(num1):
    global num
    # 上锁，如果之前没有被上锁，那么此时 上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里， 直到这个锁被解开为止
    mutex.acquire()
    for i in range(num1):
        num += 1
    # 解锁
    mutex.release()
    print("....in test1 num=%d" % num)


def test2(num1):
    global num
    mutex.acquire()
    for i in range(num1):
        num += 1
    mutex.release()
    print("....in test2 num=%d" % num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()

    # 等待上面两个线程执行完毕
    time.sleep(5)
    print("num=%d" % num)


if __name__ == '__main__':
    main()

# 互斥锁很容易出现死锁
# 下面方法可避免死锁    （添加超时时间   程序中避免--创建多个锁 按照实际情况加锁）
