"""
for  i  in  range(1,5):
          number = int(input("please input :"))
          if number > 10:
                    print("big")
          else:
                    print("loer")
i += 1
"""
"""
import time          ## import 导入函数
def decorator(func):   ##定义一个名为decorator 内置func参数
    def warpper(func_name):     ## 函数内部定义一个warpper的函数   内置func_name参数
        print(time.time())      ##打印导入的time函数里面的time
        func(func_name)
    return  warpper##定义warpper函数后返回


@decorator

def f1(func_name):    ##定义名为f1的函数
    print('this is a function'+ func_name )   ##函数内部为print打印
   # return
f1("test func")   ##调用函数传递参数
"""
"""
import time
def decorator(func):
    def wrapper(*args):   # 这里*args是通用写法，可以是别的*单词，表示任意参数/任意参数个数。多函数，多参数不用动原来的代码
        print(time.time())
        func(*args)
    return wrapper
@decorator
def f1(func_name):   # 利用装饰器的可变参数定义一个参数名
    print('This is a function ' + func_name)
@decorator
def f2(func_name1, func_name2):    # 利用可变参数定义多个参数
    print('This is a function ' + func_name1)
    print('This is a function ' + func_name2)
f1('test func')
f2('test1', 'test2')    # 调用这里要和定义保持一致
"""


def test(*args, **message):
    print(args)
    print(message)


one = (1, 2, 3)
two = {"name": "xiao", "age": "18"}
test(one, two)

test(*one, **two)
