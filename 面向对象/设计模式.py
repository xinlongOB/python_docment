# 单例设计模式
# 设计模式
#   设计模式是前人工作的总结和提炼，通常被人们广泛流传的设计模式都是针对某一特定问题的成熟的解决方案
#   使用设计模式是为了可重用代码、让代码更容易被他人理解、保证代码可靠性
# 单例设计模式
#   目的-- 让 类 创建的对象，在系统中只有唯一一个实例
#   每一次执行  类名()  返回的对象，内存地址是相同的
"""
#__new__方法






class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):   #可以传递三个参数   类     多值的元祖参数   多值的字典参数
        #1、使用类名创建  new方法会被自动调用
        print("创建对象  分配空间")
        #2、为对象分配空间    super可以调用父类方法
        instance = super().__new__(cls)

        #3、返回对象的引用
        return  instance
    def __init__(self):
        print("播放器初始化")

player = MusicPlayer()
print(player)
"""


#
class MusicPlayer(object):
    pass


# 创建多个对象
play1 = MusicPlayer()
print(play1)
play2 = MusicPlayer()
print(play2)
