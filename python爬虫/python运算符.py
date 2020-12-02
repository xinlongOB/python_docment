# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
a = 21
b = 10
c = 0

c = a + b
print"1 - c 的值为：", c

c = a - b
print
"2 - c 的值为：", c

c = a * b
print
"3 - c 的值为：", c

c = a / b
print
"4 - c 的值为：", c

c = a % b
print
"5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print
"6 - c 的值为：", c

a = 10
b = 5
c = a // b
print
"7 - c 的值为：", c
"""

#  eval 函数       将字符串当成有效的表达式 来求值  并且返回计算结果
# eval("2*5")
input_str = input("请输入算术题：")

print(eval(input_str))

import os

os.system('ls')
