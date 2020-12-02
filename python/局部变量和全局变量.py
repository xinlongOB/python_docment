"""
##在函数中定义的变量   不能再其他地方引用
def demo():
    #1、出生，执行了下面的代码才会被创建
    #2、死亡，函数执行完成之后   变量就会死亡
    num = 21
    print("函数中的变量 %s" % num)
demo()
##在函数中定义后    在其他地方引用报错
#print(num)



def demo2():
    num = 50
    print("函数中的变量 %s" % num)
demo2()
"""

##全局变量
num = 100


def demo1():
    print("demo1==> %d" % num)


def demo2():
    print("demo2==> %d" % num)


demo1()
demo2()


def demo3():
    num = 99
    print("demo3==> %d" % num)


demo3()
