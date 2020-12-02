# 定义一个函数
def test(zifu, cishu):
    print(zifu * cishu)


def test1(zifu, cishu):
    """打印多行

    :param zifu:任意字符
    :param cishu:任意次数
    """
    row = 0
    while row < 5:
        test(zifu, cishu)
        row += 1


test1("-", 10)
test1("+", 20)
