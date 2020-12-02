# 定义一个函数来分析变量是如何被引用的

def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    # 1、定义一个字符串的变量
    result = "hello"
    print("函数返回数据的内存地址是 %d" % (id(result)))
    # 2、将字符串变量返回
    return result


# 定义一个变量
a = 10

print("a 变量保存数据的内存地址是 %d" % id(a))

# 调用test函数时，本质上传递的是实参保存数据的引用，而不是实参保存的数据
r = test(a)
print("%s 的内存地址是%d " % (r, id(r)))
