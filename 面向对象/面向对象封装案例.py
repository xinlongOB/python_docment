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
    def __init__(self,model):
        #1、枪的型号
        self.model = model

        #2、子弹的数量
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        #1、判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." %self.model)

            return
        #2、发射子弹 -1
        self.bullet_count = self.bullet_count -1

        #3、提示发射信息
        print("biubiubiu     剩余子弹[%s]" % self.bullet_count)

class Role:

    def __init__(self,name):
        #1、姓名
        self.name = name
        #2、枪  - 新兵没有枪 所有指定为None
        self.gun = None

    def fire(self):
        #1、判断士兵是否有枪
        #if self.gun == None:
        if self.gun is None:
            print("[%s]还没有枪...." % self.name)
            return
        #2、高喊口号
        print("冲啊....[%s]" % self.name)
        #3、让枪装填子弹
        self.gun.add_bullet(50)
        #4、发射子弹
        self.gun.shoot()
#创建枪对象
ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()

#创建士兵对象
xusanduo = Role("许三多")

xusanduo.gun = ak47
xusanduo.fire()

##is 身份运算符
##is 用于判断两个变量引用对象是否为同一个
## == 用于判断引用变量的值是否相等
"""


# 私有属性和私有方法
# 在实际开发中，对象的某些属性和方法 可能只希望在对象的内部被使用，而不希望在外部被访问到
# 私有属性就是对象不希望公开的属性
# 私有方法就是对象不希望公开的方法

# 定义方法  ：  在定义属性或方式时，在属性名或者方法名前增加两个下划线。定义的就是私有属性或方法
class Women:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.age))


xiaofang = Women("小芳")
print(xiaofang.age)
xiaofang.secret()


##私有属性不能直接访问       方法雷同
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
print(xiaofang.__age)
xiaofang.secret()

# 科普
# 在python中，并没有真正意义的私有
# 在给属性、方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
# 处理方式：在名称前面加上_类名__名称
# 例如     print(xiaofang._Women__age)
# TODO
