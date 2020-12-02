##字典是一个无序的数据集合
##使用print函数打印字典的时候顺序会和定义的有差别

xinlong = {"name": "xinlong",
           "age": 22,
           "xingbie": "True",
           "height": 180,
           "weight": 120}
print(xinlong)
print(xinlong["weight"])

"""
##注释
xinlong = {"name" : "xin"}

##字典的基本使用
##增加
print(xinlong)
xinlong["age"]="22"
print(xinlong)

##修改    如果key不存在 就会增加一个键值对  如果存在就会修改已存在的键值对
xinlong["name"]="小小"
print(xinlong)


##删除   在删除指定键值对的时候如果不存在则报错
xinlong.pop("name")
print(xinlong)
"""

"""
xinlong = {"name" : "xin",
           "age" : 22}

##统计键值对数量
num = len(xinlong)

print(xinlong)
print(num)

##合并字典  如果被合并的字典中包含已经存在的键值对   会覆盖原有的键值对
other = {"weight" : 180}
xinlong.update(other)
print(xinlong)


##清空字典
xinlong.clear()
print(xinlong)
"""

"""
##字典的循环遍历
xinlong = {"name": "xinlong",
           "age":22,
           "xingbie" :"True",
           "height": 180,
           "weight":120}
##k是每一次循环中 获取到键值对的key
for k in xinlong:

    print("%s - %s" % (k,xinlong[k]))
"""

list = [
    {"name": "xin",
     "age": 22
     },
    {"name": "long",
     "age": 21
     }
]

for list_info in list:
    print(list_info)
