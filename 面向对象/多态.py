# 面向对象三大特性
# 1、封装  根据职责将属性和方法封装到一个抽象的 类 中
#       定义类的准则
# 2、继承 实现代码的重用，相同的代码不需要重复的编写
#       设计类的技巧
#       子类针对自己特有的需求、编写特定的代码
# 3、多态 不同的子类对象 调用父类方法 产生不同的执行结果
#       多态可以增加代码的灵活度
#        以 继承 和重写父类方法为前提
#       是调用方法的技巧、不会影响到类的内部设计

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self, ):
        print(" %s 蹦蹦跳跳的玩耍" % self.name)


class Xiaotianquan(Dog):
    def game(self):
        print("%s  飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和%s  快乐的玩耍" % (self.name, dog.name))

        dog.game()


# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = Xiaotianquan("飞天旺财")
# 创建一个人对象
xiaoming = Person("小明")

# 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
