# 子类可以拥有多个父类，并且具有所有父类的属性和方法
"""
class A():
    def test(self):
        print("A类")
class B():
    def demo(self):
        print("B类")
class C(A,B):
    #多继承可以让子类对象，同时具有多个父类的属性和方法
    pass
c = C()
c.demo()
c.test()
"""


# 多继承的使用注意事项   （如果不同的父类中存在同名的方法）
# 提示：在开发是，应该尽量避免这种容易产生混淆的情况
# --如果父类之间存在同名的属性或者方法。应该避免使用多继承
class A():
    def test(self):
        print("A类--test")

    def demo(self):
        print("A类--demo")


class B():
    def test(self):
        print("B类--test")

    def demo(self):
        print("B类--demo")


class C(A, B):
    # 父类之间存在同名的属性或者方法的多继承  那个先继承 调用那个父类的属性和方法
    pass


c = C()
c.demo()
c.test()


def test():
    if 0 == 0:
        print("ok")


if __name__ == '__main__':
    test()
