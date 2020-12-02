##str  bytes的相互转换
##编码方式和解码方式必须一样 否则出现乱码
a = "米花互动"
print(type(a))

b = a.encode()

print(type(b))

##bytes 解码为str
c = b.decode()
print(type(c))

test = b.decode("utf-8")
print(test)

# python2  如果想处理中文需要指定解释器
# conding=utf8
# *-* coding:utf8 *-*
import logging

n = 1
while n < 10:
    print("n是   %d" % n)
    k = n % 2
    print("目前是 %d" % k)
    if k == 0:
        pass
    else:
        pass
    # print(n)
    n = n + 1
