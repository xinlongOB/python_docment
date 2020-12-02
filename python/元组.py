##定义一个元祖
##快速查看元祖提供哪些操作   定义一个元祖   然后元祖变量名+.  例如  info = ()        info.  然后TABLE补全

"""
info_tuple = ("zhangsan",18,180)
##打印元祖中的数据
info_tuple[1]

print(info_tuple[1])


##定义一个空元祖
sing_tuple = ()


##定义一个固定一个元素的元祖

##如果直接写成set_tuple = (12)  此时的类型为int 整数型
set_tuple = (12,)

itype = type(set_tuple)

print("此时元祖set_tuple 的类型是 %s" % itype)

print(set_tuple[0])


##元祖的基本操作
table = ("xinlong",180,18)

##取值和索引
print(table[1])
## 已知道数据内容，取出数据在元祖中的索引
print(table.index("xinlong"))

##统计数据个数
print(table.count("xinlong"))

##统计元祖中包含元素个数
lens = (len(table))
print("当前元祖包含 %d" % lens)

##格式化字符串后面的"()"本身就是元祖
str = ("bad",21,1.85)
print("%s 的年龄是 %d  身高是%.2f" % ("bad",21,1.85))
print("%s 的年龄是 %d  身高是%.2f" % str)

##列表和元祖之间得转换
name_list = ["xinlong","long","liangxinlong"]
print(type(name_list))
##当前name_list是个列表如果不希望别人修改列表可以转换成元祖，使用tuple这个函数
modfiy = tuple(name_list)
##name_list列表转换成为元组后，需要重新定义一个变量名
print(type(modfiy))

##如果想要修改元组数据的内容 使用list函数转为列表
remod = list(modfiy)
print(type(remod))
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
a, b = (b, a)
##提示：等号右边是一个元祖，只是把小括号省略了
# a,b = b,a
print(a)
print(b)
