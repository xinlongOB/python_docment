# 在父类定义的私有方法或属性   子类不能直接访问
"""
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % self.num1,self.__num2)
class B(A):
    def demo(self):
        pass
        #1、访问父类的私有属性
       # print("访问父类的私有属性 %d" % self.__num2)
        #2、调用父类的私有方法
        #super().__test()
b = B()

print(b)

#在外界不能直接访问对象的私有属性/调用私有方法
print(b.num1)
#print(b.__num2)
b.demo()
"""


# 在父类定义的私有方法或属性   子类可以直接访问

# 子类可以通过间接的方式调用父类的私有方法和属性
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的共有方法 %d" % self.__num2)
        self.__test()

        # self.__test()


class B(A):
    def demo(self):
        # 1、访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 2、不可以调用父类的私有方法
        # 3、访问父类的公有属性
        print("子类方法 %d" % self.num1)
        # 4、调用父类的公有方法
        self.test()
        # super().__test()
        # b.test()


b = B()
# print(b)
# 在外界不能直接访问对象的私有属性/调用私有方法
print(b.num1)
# print(b.__num2)
b.demo()
