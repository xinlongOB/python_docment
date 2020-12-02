"""
##在类的封装中，第一个参数必须是self

##小猫爱吃鱼    小猫要喝水

#分析
#类   猫
#动作    吃  喝水
#按照需求 -- 不需要定义属性

#创建类
class Cat:
    #创建动作
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")
#创建对象
tom = Cat()

##调用动作
tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print("%x" % addr)
##%d可以以10进制输出数字
##%x可以以16进制输出数字


##在创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

lazy_cat2 = lazy_cat
"""

# 在外部临时添加属性 （如果定义属性在调用对象之后   会报错）
"""
##创建类
class Cat:
    #创建动作
    def eat(self):
        ##哪一个对象调用的方法，self就是那一个对象的引用
        #print("小猫爱吃鱼")
        print("%s 爱吃鱼" % self.name)
    def drink(self):
        print("%s 要喝水" % self.name)
#创建对象
tom = Cat()
#可以使用 .属性名  利用赋值语句就可以了
tom.name = "kin"
##调用动作
tom.eat()
tom.drink()
#print(tom.name)

lazy_tom = tom
lazy_tom.name = "懒猫"

lazy_tom.drink()
lazy_tom.eat()

##可以通过self. 访问对象的属性
##可以通过self. 调用其他的对象方法
"""

##提示： 在日常开发中，不推荐在类的外部给对象添加属性
## 如果在运行时，没有找到属性，程序会报错
## 对象应该包含哪些属性，应该封装在类的内部


##初始化以及定义属性
"""
##当使用类名(类名（）)创建对象时，会自动执行一下操作
    #1、为对象在内存中分配空间--创建对象
    #2、为对象的属性设置初始值--初始化方法（init）
    #这个初始化方法就是__init__方法， __init__是对象的内置方法
       ##     这个方法专门用来定义一个类具有哪些属性的方法
class Cat:
    def __init__(self):
        print("这是一个初始化方法")
        ##在内部self.属性名 = 属性的初始值
        self.name = "kin"
    def eat(self):
        print("%s 爱吃鱼" % self.name)
#当使用类名创建对象的时候，会自动调用初始化方法__init__
tom = Cat()
tom.eat()
#print(tom.name)
"""

##利用参数设置属性初始值
"""
#在开发中，如果希望在创建对象的同时，就设置对象的属性，可以对__init__方法进行改造
#1、把希望设置的属性值，定义成__init__方法的参数
#2、在方法内部使用self.属性名 =  形参  接受外部传递的参数
#3’在创建对象时，使用类名（属性1、属性2.。。）调用
class Cat:
    def __init__(self,name):
        print("这是一个初始化方法")
        ##在内部self.属性名 = 属性的初始值
        #self.name = "kin"
        self.name = name
    def eat(self):
        print("%s 爱吃鱼" % self.name)
#当使用类名创建对象的时候，会自动调用初始化方法__init__
tom = Cat("kin")
tom.eat()

lazy_cat = Cat("懒猫")
lazy_cat.eat()

"""


##内置方法和属性  __del__    and    __str__
# 当使用类名创建对象时。为对象分配空间后，自动调用__init__方法
# 当一个对象被对象从内存中销毁前，会自动调用__del__方法

# 应用场景
# __init__改造初始化方法，可以让创建的对象更加灵活
# __del__如果希望在对象被销毁前，在做一些事情，可以考虑下__del__方法

# 生命周期
# 1、一个对象从调用类名创建，生命周期开始
# 2、一个对象的__del__方法一旦被调用，生命周期结束
# 3、在对象的生命周期内，可以访问对象属性，或者让对象调用方法
class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):
        ##__str__ 必须返回一个字符串
        return "我是小猫[%s]" % self.name


# tom是一个全局变量，当全部代码执行结束后，才会执行__del__内置方法
tom = Cat("Tom")
# print(tom.name)
##del 关键字可以删除一个对象
# del tom

# print("-" * 50 )

##__str__ 必须返回一个字符串
print(tom)
