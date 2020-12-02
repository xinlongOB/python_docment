# 关于是否使用global
"""
# 函数里面修改全局变量
# 关于是否加 global  如果使用 +=  或者 -= 必须加上
# 如果是调用append  或者insert  只要是指定的内存地址不变  就不用加global

# 要看是否对 全局变量的执行指向进行修改
# 如果修改了执行，既让全局变量指向了一个新的地方，那么必须使用global
# 如果仅仅是修改了指向的空间中的数据，此时不用必须使用global
# 例如：

num = 100
def test():
    global num
    num += 100
print(num)  # 调用函数前打印
test()
print(num)  # 调用函数 在打印

nums = [11,22]
def test2():
    nums.append("33")

print(nums)
test2()
print(nums)
"""

# 验证线程共享全局变量
"""
import time
import threading

# 定义一个全局变量
num = 100

def test1():
    global  num
    num += 1
    print("....in test1 num=%d" % num)

def test2():
    print("....in test2 num=%d" % num)

def  main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    print("num=%d" % num)


if __name__ == '__main__':
        main()
        
"""

# 参数传递
"""
import time
import threading

# 定义一个全局变量


def test1(temp):
    print(temp)
    temp.append("33")
    print("....in test1 temp=%s" % str(temp))


def test2(temp):
    print("....in test2 temp=%s" %str(temp))

num = [11,22]

def main():
    # target 指定这个线程去哪个函数执行代码
    # args 指定将来调用函数的时候 传递什么数据过去
    t1 = threading.Thread(target=test1,args=(num,))
    t2 = threading.Thread(target=test2,args=(num,))
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)
    print("num=%s" % num)


if __name__ == '__main__':
    
    main()

"""

# 验证线程共享全局变量    两个函数同时操作全局变量
"""
import time
import threading

# 定义一个全局变量
num = 0

def test1(num1):
    global num
    for i in range(num1):
        num += 1
    print("....in test1 num=%d" % num)


def test2(num1):
    global num
    for i in range(num1):
        num += 1
    print("....in test2 num=%d" % num)


def main():
    t1 = threading.Thread(target=test1,args=(100,))
    t2 = threading.Thread(target=test2,args=(100,))
    t1.start()
    t2.start()

    # 等待上面两个线程执行完毕
    time.sleep(5)
    print("num=%d" % num)

if __name__ == '__main__':
    main()

"""

# 把传递的数据变大
import time
import threading

# 定义一个全局变量
num = 0


def test1(num1):
    global num
    for i in range(num1):
        num += 1
    print("....in test1 num=%d" % num)


def test2(num1):
    global num
    for i in range(num1):
        num += 1
    print("....in test2 num=%d" % num)


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

# 这样 这里最后num 的变量是不正确的
