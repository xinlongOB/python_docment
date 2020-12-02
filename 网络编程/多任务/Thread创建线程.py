"""
查看代码应该从调用开始查看

Thread(target=sing)
就是创建一个对象


threading.enumerate  可以返回当前所有的线程数
"""

# 通过继承Thread类 完成创建线程
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name + '@' + str(i)
            print(msg)

    def login(self):
        pass

    def pay(self):
        pass


if __name__ == "__main__":
    t = MyThread()
    t.start()  # 调用对象  会自动调用函数 run    这个函数名必须是run
    # login和pay两个函数 需要在run函数里面调用
