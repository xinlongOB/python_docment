# 进程
# 程序： 例如xxx.py这是程序，是一个静态的
# 进程： 一个程序运行起来后，代码+用到的资源 称之为进程，它是操作系统分配资源的基本单元，
#       不仅可以通过线程完成多任务，进程也是可以的

# 进程的状态
# 工作中，任务数大于cpu的核数，即一定有一些任务正在执行，而另外一些任务在等待cpu进行执行
#       因此导致有了不同的状态


# 回顾多线程
"""
import  threading
import  time


def test1():
    print("1111")
    time.sleep(1)


def test2():
    print("2222")
    time.sleep(2)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
	

if __name__ == "__main__":
	main()
"""

import time
import multiprocessing  # 导入进程模块


def test1():
    while True:
        print("111")
        time.sleep(1)


def test2():
    while True:
        print("222")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
