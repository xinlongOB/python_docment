"""
#需求 1、小明体重75.0公斤
#     2、小明名词跑步会减肥0.5公斤
#     3、小明每次吃东西体重增加1公斤

class ren:

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 1

    def run(self):
        self.weight -= 0.5

xiaomei = ren("小美",75)
xiaomei.eat()

print(xiaomei.weight)
"""
"""
#需求 1、房子(House)有户型、总面积 和 家具名称列表
#           新房子没有任何家具
#     2、家具(HouseItem)有名字 和 占地面积 其中
#           席梦思(bed)占地 4 平米
#           衣柜(chest)占地 2 平米
#           餐桌(table)占地 1.5 平米
#      3、将以上三件家具添加到房子中
#      4、打印房子时，需要输出：户型、总面积、剩余面积、家具名称列表

#剩余面积
#1、创建房子对象时，定义一个剩余面积的属性，初始值和总面积相等
#2、当调用add_item方法，向房间添加家具时，让剩余面积 -=家具面积

#说明：应该先开发家具类  家具类简单  并且房子需要使用到家具，被使用的类，通常应该先开发
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return ("%s 占地面积 %.2f" % (self.name,self.area))

class House:
    def __init__(self,name,allarea):
        self.name = name
        self.allarea = allarea
        self.free_area = allarea
        self.itemlist = []

    def __str__(self):
        return ("户型：%s\n 总面积是:%.2f\n  剩余面积:%2.f\n  家具列表:%s\n" % (self.name,self.allarea,self.free_area,self.itemlist))

    def add_item(self,name):
        if name.area > self.free_area:
            print("%s 的面积太大了" % name.name)
            return

        self.itemlist.append(name.name)

        self.free_area -= name.area

bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)

print(bed)
print(chest)
print(table)

house = House("别墅",150)
house.add_item(bed)

print(house)
"""

"""
#需求
#士兵 许三多有一把AK47
#士兵可以开火
#枪能够发射子弹
#枪能够装填子弹--增加子弹数量

#分析
#需要定义一个类   士兵
#动作：士兵name是许三多   士兵可以开枪
#属性：许三多有个AK47  需要调用枪类

#需要定义一个类  枪类
#
#动作：发射子弹
#属性：子弹数量

#那个类被调用   就先创建那个类
class Gun:
    def __init__(self,mode):
        self.mode = mode
        self.count = 0

    def add_count(self,countnum):
        self.count += countnum

    def shoot(self):
        if self.count <= 0:
            print("%s 没子弹" %self.mode)
            return
        print("biubiubiu")
        self.count -= 1
ak = Gun("AK47")
ak.add_count(50)
ak.shoot()
print(ak.count)
"""

"""
name1 = {
    "a" : "qq",
    "b" : "18"
}
name2 = {
    "name" : "ww"
}

print(name1)
name1.update(name2)
print(name1)

list = ["2","3","5"]
list.append("6")
print(list)
"""


class Animal():
    def run(self):
        pass

    def eat(self):
        print("吃")


class Dog(Animal):
    def bark(self):
        print("汪汪汪")


# 继承
wangcai = Dog()


# wangcai.eat()
class Xiao(Dog):
    def fly(self):
        print("起飞")

    def bark(self):
        print("niuniuniu")


quan = Xiao()
quan.fly()
quan.bark()
