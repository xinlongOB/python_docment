import time  ## import 导入函数


def decorator(func):  ##定义一个名为decorator 内置func参数
    def warpper():  ## 函数内部定义一个warpper的函数   内置func_name参数
        print(time.time())  ##打印导入的time函数里面的time
        func()

    return warpper  ##定义warpper函数后返回


@decorator
# def f1(func_name):    ##定义名为f1的函数
#   print('this is a function' + func_name)   ##函数内部为print打印

def test():
    print("test")


f = decorator(test)  ##调用函数传递参数
f()

"""
def measure():
    ##测量温度和湿度
    print("测量开始...")
    temp = 39
    wetness =50
    print("测量结束...")
    ##元祖可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    ##如果函数返回的类型是元祖，小括号可以省略
    return temp,wetness
##result 此时的类型是元祖
result = measure()
print(result)

##需要单独处理温度或者湿度
print(result[0])
print(result[1])

##如果函数返回的类型是元祖，同事希望单独处理元祖中的元素
##可以使用多个变量，一次接收函数的返回结果
##注意：使用多个变量结束结果时，变量的个数和元祖中的元素个数保持一致
gl_wen,gl_shi = measure()
print(gl_wen)
print(gl_shi)
"""
a = 6
b = 100

# 解法1：使用变量
# c = a
# a = b
# b = c

# 解法2：不适用其他的变量
# a = a + b
# b = a - b
# a = a - b


# 解法3：python专有写法  a接收b的元素   b接收a的元素
# a,b = (b,a)
##提示：等号右边是一个元祖，只是把小括号省略了
a, b = b, a
# print(a)
# print(b)
