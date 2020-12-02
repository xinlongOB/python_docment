# 不使用继承
"""
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")
    def brak(self):
        print("叫")

wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.brak()
"""
# 继承的语法
"""
#继承就是  子类拥有父类的所有方法和属性
class Animal:
    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")

class Dog(Animal):
    def brak(self):
        pass

wangcai = Dog()
wangcai.sleep()

##子类继承父类，可以直接 使用父类中已经封装好的方法，不需要再次开发
##子类中应该根据职责，封装子类特有的属性和方法
#调用示例
#class 类名(父类)
#class Dog(Animal)
#

#专业术语
#Dog类是Animal类的子类，Animal类是Dog类的父类，Dog类从Animal类继承
#Dog类是Animal类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生
class Xiaotianquan(Dog):
    def fly(self):
        print("飞")

quan = Xiaotianquan()
quan.fly()
quan.sleep()
quan.drink()

#继承的传递： 子类拥有父类以及父父类的属性和方法
"""

# 重写
# 1、覆盖父类的方法
"""
#2、对父类方法进行扩展
class Animal:
    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")

class Dog(Animal):
    def brak(self):
        print("汪汪汪")

wangcai = Dog()

class Xiaotianquan(Dog):
    def fly(self):
        print("飞")
    def brak(self):
        print("神狗叫法")

quan = Xiaotianquan()
quan.brak()

#如果子类中，重写了父类的方法
#在使用子类对象调用方法时，会调用子类中重写的方法
"""


# 重写--->扩展
# 1、首先在子类中重写父类的方法
# 2、在需要的位置使用super().父类方法   来调用方法的执行
# 3、代码其他的位置针对子类的需求’编写子类特有的代码实现

class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("汪汪汪")


class Xiaotianquan(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        # 1、针对子类特有的需求，编写代码
        print("神狗叫法")
        # 2、使用super（）. 调用原本父类中封装的方法
        super().bark()
        # 3、添加其他子类的代码
        print("66666666")


quan = Xiaotianquan()
quan.bark()
