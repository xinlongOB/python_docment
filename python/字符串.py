##双引号和单引号的作用
"""
str = "我是谁"
print(str)
str1 = '我是"谁"'
print(str1)
"""

"""
##从字符串中提取字符
str = "hello python"
##提取里面的y
print(str[7])

##for 循环遍历字符串中每一个字符
for c in str:
    print(c)
"""

"""
##  统计字符串长度     统计一个子字符串在大字符串出现的次数     查看子字符串在大字符串中的第一次出现的索引

str = "hello  world"


## 统计字符串长度
print(len(str))

##统计一个子字符串在大字符串出现的次数    如果不存在不会报错  会显示出现0次
print(str.count("l"))

##取出索引   如果不存在则会报错
print(str.index("d"))
print(str.index("K"))
"""

"""
##字符串的操作---判断类型        
# ##网站：https://blog.51cto.com/13673885/2362950       https://www.cnblogs.com/easyidea/p/10382271.html
##判断字符串中是否只包含空格   如果只包含空格会显示True  否则打印false     \t \n \r都属于空格
space_str = " \t \n \r"
print(space_str.isspace())

#判断字符串至少有一个字符并且所有字符都为字母或数字则返回True   （有一个空格或者符号都返还false）
alnum = "kuaiwan1904"
print(alnum.isalnum())

#判断字符串至少有一个字符并且所有字符都为字母则返回True   （有一个空格、数字或者符号都返还false）
alpha = "string"
print(alpha.isalpha())

#判断字符串只包含数字则返回True
##   isdigit   isdecimal  isnumeric    三个方法都不能判断小数
##    isdigit 可以判断unicode字符串   例如：\u00b2      isnumeric  可以判断中文数字  例如：一千零一
digit = "942868591"
print(digit.isdigit())

#判断字符串是标题化的(每个单词的首字母大写)则返回 True  (单词首字母不是大写则返回false）
title = "My Nmae Is Long"
print(title.istitle())

#判断字符串全是小写
lower = "abc"
print(lower.islower())

#判断字符串全是大写
upper = "PWD"
print(upper.isupper())

"""

"""
##字符串的操作---查找和替换
##检查字符串是否是以 na 开头，是则返回 True
start = "name is xxx"
print(start.startswith("na"))

##检查字符串是否是以 xxx结束，是则返回 True
end = "name is xxx"
print(end.endswith("xxx"))

## 检测 server 是否包含在 string 中，如果 start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 -1
find = "all the servers is Ok and set ableConnect"
##查找find字符串中是否包含server
print(find.find("server"))
##查找find字符串中是否包含server   开始索引0   结束索引20
print(find.find("server",0,20))

##类似于 find()，不过是从右边开始查找
rfind = "all the servers is Ok and set ableConnect"
print(rfind.rfind("server"))

##跟 find() 方法类似，不过如果 str 不在 string 会报错
index = "all the servers is Ok and set ableConnect"
print(index.index("server"))

##类似于 index()，不过是从右边开始
rindex = "all the servers is Ok and set ableConnect"
print(rindex.rindex("server"))

## 把 string 中的 all 替换成 two，如果 num 指定，则替换不超过 num 次
replace = "all the servers is Ok and set ableConnect  all  all  all"
##把 string 中的 all 全部替换成 two
print(replace.replace("all","two"))
##把 string 中的前两个 all 替换成 two
print(replace.replace("all","two",2))
"""

"""
##字符串的操作---大小写转换
##把字符串的第一个字符大写
capitalize = "all the servers is Ok and set ableConnect"
print(capitalize.capitalize())

##把字符串的每个单词首字母大写
title = "all the servers is Ok and set aBleConnect"
print(title.title())

##转换 string 中所有大写字符为小写
lower = "All The Servers Is Ok And Set Ableconnect"
print(lower.lower())

##转换 string 中所有小写字母为大写
upper = "all the servers is ok and set ableconnect"
print(upper.upper())

## 翻转 string 中的大小写
swapcase = "A b C d E f"
print(swapcase.swapcase())
"""

"""
##字符串的操作---文本对齐
##返回一个原字符串左对齐      例如str.ljust(width[, fillchar])      width是个数  fillchar是填充符 默认空格
just = "all the servers is Ok and set ableConnect"
## 49 意思就是加上原来的字符串 一共的长度  +为填充符
print(just.ljust(49,"+"))

##返回一个原字符串右对齐
print(just.rjust(49,"+"))

print(just.center(49,"+"))
"""

"""
##字符串的操作---去除空白字符
str = "       all the servers is Ok and set ableConnect      "
print(str)
##截掉 string 左边（开始）的空白字符
print(str.lstrip())
##截掉 string 右边（开始）的空白字符
print(str.rstrip())
##截掉 string 左右两边的空白字符
print(str.strip())
"""

"""
##字符串的操作---拆分和连接
##把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
partition = "all the servers is Ok and set ableConnect"
print(partition.partition("the"))

##类似于 partition() 方法，不过是从右边开始查找
print(partition.rpartition("the"))

##string.split(str="", num) | 以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格

pome = "登鹤雀楼 \t  王之涣  \t  白日依山尽  \t \n  黄河入海流  \t  \t 欲穷千里目   \n  更上一层楼"
print(pome)
pome_list = pome.split()
print(pome_list)

lastpome = " ".join(pome_list)
print(lastpome)

print(lastpome.replace(" ","\n"))
"""

##字符串切片
num_str = "0123456789"
##1、截取从2 - 5位置的字符串
print(num_str[2:6])
##2、截取2 - 末尾的字符串
print(num_str[2:])
##3、截取从开始 - 5 位置的字符串
print(num_str[:6])
##4、截取完整的字符串
print(num_str[:])
##5、从开始位置，每隔一个字符截取字符串
print(num_str[::2])
##6、从索引 1 开始，每隔一个取一个
print(num_str[1::2])
##7、截取从2 - 末尾 -1  的字符串
print(num_str[2:-1])
##8、截取字符串末尾两个字符
print(num_str[-2:])
##9、字符串的逆序
print(num_str[-1::-1])
