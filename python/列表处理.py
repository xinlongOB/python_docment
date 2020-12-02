##定义一个列表

##快速查看元祖提供哪些操作   定义一个元祖   然后元祖变量名+.  例如  info = ()        info.  然后TABLE补全

name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer", "wangwu", "wangxiaoer"]
num_list = ["1", "3", "2", "0"]

##导入一个模板
##import 函数
##函数.test("-",20)
##print(函数.name)


##增加列表内的指定参数索引和参数
##name_list.insert(0,"long")

##增加另一个列表内容到此列表中
name_list.extend(num_list)

##增加一个参数到列表末尾
# name_list.append("wangbadan")

##删除列表内的指定参数

##name_list.remove("zhangsan")

##删除列表内最后一个参数

##name_list.pop()

##修改列表内的参数

##name_list[1] = "xinxin"

##清空列表中的数据
##name_list.clear()

##统计列表长度
##length = len(name_list)
##print(length)

##统计数据在列表中出现的次数
##num = name_list.count("wangxiaoer")
##print(num)
##打印列表

##列表中数据排序

num_list.sort()

name_list.append("ceshi")
name_list.append("ceshi")
name_list.append("ceshi")
name_list.remove("ceshi")
print(name_list)
print(num_list)
