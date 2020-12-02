##使用元祖接收函数之后后返回的多个值
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
##python专属替换两个变量的值
"""
a = 6
b = 100

#解法1：使用变量
#c = a
#a = b
#b = c

#解法2：不适用其他的变量
#a = a + b
#b = a - b
#a = a - b


#解法3：python专有写法  a接收b的元素   b接收a的元素
#a,b = (b,a)
##提示：等号右边是一个元祖，只是把小括号省略了
a,b = b,a
print(a)
print(b)
"""
##在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
"""
def  demo(num,num_list):
    print("函数内部的代码")
    ##在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    num = 100
    num_list = [1,2,3]

    print(num)
    print(num_list)
    print("函数执行完成")

gl_num = 99
gl_list = [4,5,6]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)
"""
##使用方法修改了数据的内容，会影响到外部的数据   （次修改不是重新定义变量，而是直接修改append或者是remove）
"""
def  demo(nul_list):
    print("函数内部的代码")
    #使用方法修改列表的内容
    #使用方法修改了数据的内容，会影响到外部的数据   （次修改不是重新定义变量，而是直接修改append或者是remove）
    nul_list.append(9)
    print(nul_list)
    print("函数执行完成")
gl_list = [1,2,3]
demo(gl_list)
print(gl_list)
"""
##列表变量使用 + 不会做相加在赋值的操作
"""
def demo(num,num_list):
    print("函数开始")
    # num += num  就是 num = num + num   数字是先相加在赋值
    num += num

    #num_list  = num_list + num_list
    #列表变量使用 + 不会做相加在赋值的操作
    #本质是在调用列表的extend方法
    ##增加另一个列表内容到此列表中
    ##name_list.extend(num_list)
    #num_list.extend(num_list)
   # num_list += num_list
    ##这样才是先相加在赋值
    num_list = num_list + num_list
    print(num)
    print(num_list)
    print("函数完成")
gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)
"""
##缺省参数
"""
##缺省参数，就是讲常见的值设为参数的缺省值，从而简化函数的调用
gl_list = [6,3,9]
#默认按照升序排序
gl_list.sort()
print(gl_list)
##如果需要降序排序，需要执行reverse参数
gl_list.sort(reverse=True)
print(gl_list)
"""


##定义函数指定缺省参数     需要在末尾指定  不然后面无法写参数

def print_info(name, gender=True):
    # :param name:同学姓名
    #:param gender: True  男生  False 女生
    #:return:

    gender_text = "男生"
    print(gender)
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


##提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值
# print_info("小明",True)
# print_info("小明")
# print_info("老王")
# print_info("小美",False)
print_info("小明")

##多值参数
"""
def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)

#demo(1)
demo(2,3,4,5,name = "小明",age = 18)
"""
##多值参数--数字累加
"""
def sum_numbers(*args):
    num = 0
    print(args)
    for  n  in  args:
        num += n
    return  num
result = sum_numbers(1,2,3,4,5)
print(result)
"""

##递归
"""
def sum_numbers(num):
    print(num)
    #递归的出口，当参数满足某个条件，不在执行参数
    if num == 1:
        return
    #递归的特点就是自己调用自己
    sum_numbers(num - 1)

sum_numbers(3)
"""

##递归是一个编程技巧。初次接触递归会感觉有些吃力，在处理不确定
##的循环条件是，格外有用， 例如：遍历整个文件目录的结构
"""
def sum_numbers(num):
    #1、定义出口
    if num == 1:
        return 1
    #2、数字的累加 num + （1...num -1)
    #假设sum_numbers 能够正确的处理 1...num -1
    temp = sum_numbers(num - 1)
    #两个数字的相加
    return  num + temp
result = sum_numbers(100)
print(result)
"""
