# 类的术语     --实例
# 1、使用面向对象开发、第一步是设计类
# 2、使用类名()创建对象。创建对象的动作有两步：
#       1、在内存中为对象创建分配空间
#       2、调用初始化方法__init__为对象初始化
# 3、创建对象后，内存中就有了一个对象的实实在在的存在  --实例

# 因此 通常也会把
# 1、创建出来的对象叫做类 的实例
# 2、创建对象的动作叫做实例化
# 3、对象的属性叫做实例属性
# 4、对象调用的方法叫做实例方法

# 类是一个特殊的对象

# 创建类方法示例

class Game(object):

    @classmethod
    def leiming(cls):  # cls  和self 一样 是第一个参数  可以不传递
        pass


# 类可以定义属性和方法   叫做 类属性    类方法
# 类属性就是给类对象中定义的属性
# 通常用来记录 与这个类相关的特征
# 类属性不会用户记录具体对象的特征
"""
#示例需求
#定义一个工具类
#每个工具都有自己的name
#需求--知道使用这个类，创建了多少个工具对象
class Tool(object):
    #使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self,name):
        self.name = name

        #让类属性的值+1
        Tool.count += 1

#1、创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

#2、输出类属性的数量
print(Tool.count)
"""

# 在python中属性的获取存在一个向上查找机制
# 首先在对象内部查找对象属性  如果没有就去类属性中查询


# 静态方法
"""
#在开发时，如果需要在 类中封装一个方法 这个方法既不需要方式实例属性 或者调用势力方法
#       也不需要访问类属性或者调用类方法
#这个时候 可以把这个方法封装成一个静态方法

#语法如下：
#@staticmethod
#def  静态方法名称():
#    pass
#静态方法需要使用修饰器 #staticmethod 来标识，告诉解释器这是一个静态方法
#通过类名.调用静态方法
class Dog(object):
    @staticmethod
    def run():

        #不访问实例属性/类属性
        print("跑步")

#通过类名.调用静态方法  -- 不需要创建对象
Dog.run()
"""


# 方法总和案例
# 需求
# 1、设计一个Game 类
# 2、属性：
#       定义一个类属性 top_seore记录游戏的历史最高分
#       定义一个势力属性 player_name记录当前游戏的玩家姓名
# 3、方法：
#   静态方法show_help显示游戏帮助信息
#   类方法 show_top_score 显示历史最高分
#   案例方法start_game 开始当前玩家的游戏
# 4、主程序步骤
#   1、查看帮助信息
#   2、查看历史最高分
#   3、创建游戏对象 开始游戏
class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("游戏说明：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("let's  go ")


# 1、查看游戏的帮助信息
Game.show_help()
# 2、查看历史最高分
Game.show_top_score()
# 3、创建游戏对象
xiaoming = Game("小明")
xiaoming.start_game()

# 本节总结
# 1、实例方法--方法内部需要访问案例属性
#   实例方法内部可以使用类名.访问类属性
# 2、类方法--内部只需要 访问类属性
# 3、静态方法-- 方法内部、不需要实例属性和类属性

# 如果方法内部即需要访问实例属性、又需要访问类属性。应该定义成实例方法
# 因为类只有一个 在实例方法内部可以使用类名.访问类属性
