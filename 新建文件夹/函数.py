# import 最简单的服务器.py
# 最简单的服务器.monitor()

"""
def age(n):
    if n == 1:c = 10
    else:
        c = age(n - 1) + 2
#        print(n)
    return c


print(age(5))
"""


def test(a):
    if a == 1:
        c = 1
    else:
        c = + test(a - 1) + 1
    #        print(a)
    return c


print(test(365))

# !/usr/bin/env python

n = 1
s = 0
while n < 365:
    s = s + n
    n = n + 1

print(s)
