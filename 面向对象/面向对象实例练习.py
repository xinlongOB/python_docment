## 封装
# 1、封装是面向对象编程的一大特点
# 2、面向对象编程的第一步--将属性和方法封装到一个抽象的类中
# 3、外界使用类创建对象、然后让对象调用方法
# 4、对象方法的细节都被封装在类的内部

# 需求 1、小明体重75.0公斤
#     2、小明名词跑步会减肥0.5公斤
#     3、小明每次吃东西体重增加1公斤
"""
class Person():
    def __init__(self,name,weight):
        #self.属性 = 形参
        self.name = name
        self.weight = weight
    def __str__(self):
        return "我的名字是 %s  体重是 %.2f 公斤" % (self.name,self.weight)
    def run(self):
        print("%s 爱跑步" % self.name)
        self.weight -= 0.5
    def eat(self):
        print("%s 是吃货"% self.name)
        self.weight += 1
xiaoming = Person("小明",75)
xiaoming.eat()
xiaoming.run()
print(xiaoming)

xiaomei = Person("小美",45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)

#由上列代码可看出   在对象的方法内部，是可以直接访问对象的属性的
##  同一个类创建的多个对象之前，属性互不干扰
"""


# 需求 1、房子(House)有户型、总面积 和 家具名称列表
#           新房子没有任何家具
#     2、家具(HouseItem)有名字 和 占地面积 其中
#           席梦思(bed)占地 4 平米
#           衣柜(chest)占地 2 平米
#           餐桌(table)占地 1.5 平米
#      3、将以上三件家具添加到房子中
#      4、打印房子时，需要输出：户型、总面积、剩余面积、家具名称列表

# 剩余面积
# 1、创建房子对象时，定义一个剩余面积的属性，初始值和总面积相等
# 2、当调用add_item方法，向房间添加家具时，让剩余面积 -=家具面积

# 说明：应该先开发家具类  家具类简单  并且房子需要使用到家具，被使用的类，通常应该先开发

# 定义家具类
class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表名称
        self.items_list = []

    def __str__(self):
        # pyhon可以自动将一括号内部的代码连接在一起
        return ("户型：%s\n 总面积：%.2f \n剩余面积：%.2f \n 家具：%s" %
                (self.type, self.area, self.free_area, self.items_list))

    def add_item(self, item):
        # 1、判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了" % item.name)
            return
        # 2、将家具的名称添加到列表中
        self.items_list.append(item.name)
        # 3、计算剩余面积
        self.free_area -= item.area


# 创建对象(家具)
bed = HouseItem("席梦思", 190)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 15)

print(bed)
print(chest)
print(table)

# 创建房子
my_home = House("别墅", 200)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)

##主程序只负责创建房子和家具的对象
##让房子对象调用add_itme方法将家具添加到房子中
##面积计算、剩余面积、家具列表等都被封装到房子类的内部
