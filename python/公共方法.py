"""
##max  min 两个函数的作用       如果对比字典  max 和min之比较两个key的大小 不取值
num_list = "942868591"
##取出最大数
print(max(num_list))
##取出最小数
print(min(num_list))

##函数len   del作用
list = ["a","b","c"]
print(len(list))

##del  删除列表中索引为1的数据
del list[1]
print(list)
"""

"""
##列表和元祖的切片       字典不可以进行切片
num_str = "0123456789"
##1、截取从2 - 5位置的字符串
print(num_str[2:6])

yuanzu = [0,1,2,3,4,5,6,7,8,9]
print(yuanzu[2:6])

liebiao = (0,1,2,3,4,5,6,7,8,9)
print(yuanzu[2:6])
"""

"""
##*运算符     字符串和字典和列表支持 *    但是字典不支持 *     因为字典里面的key是唯一的
print([1,3,4] * 3)

print((1,3,4) * 3)

print("1,3,4" * 3)

## +  运算符
print("hello" + "python")

print(["12"] + ["34"])

print(("12") + ("34"))
"""

"""
"a" in "abc"
True
"a" not in  "abc"
False

##  in  和 not  in   是判断前面的子字符是否在字符串中     同样 列表、元祖都可以使用     字典只能判断前面的是否是key   不能判断数据
"""

"""
##完整的for循环
for i in [1,2,3,4,5]:

    print(i)
    if i == 3:
        break
else:
    ##如果循环体内部使用了break退出了循环 就不会打印
    print("for循环完成后打印")

print("执行完毕")
"""

students = [
    {"name": "张三",
     "age": "20"},
    {"name": "李四",
     "age": "21"},
    {"name": "王五",
     "age": "22"}
]

find_name = "王五"
for name in students:
    if name["name"] == find_name:
        students.remove(name)
        print("已删除")

print(students)

"""
find_name = "王五"

##print(students[1]["name"])
for name in students:

    if name["name"] == find_name:

        print("找到了  %s" % name)
        break
else:
    print("未找到 %s" % find_name)

print("循环结束")
"""
