"""
派生精灵子类
新建plane_sprites.py文件
定义GameSprite 继承自pygame.sprite.Sprite

注意：如果一个类的父类不是object
      在重写初始化方式时，一定要先 super()一下父类的__init__方法
      保证父类中实现__init__代码能够被正常执行

GameSprite   ：image      rect      speed
            __init__(self,image_name,speed=1):
            update(self):

属性：image 精灵图像、使用image_name 加载
      rect 精灵大小、默认使用图像大小
      speed 精灵移动速度，默认为 1
方法  update 每次更新屏幕时在游戏循环内调用
      让精灵的self.rect.y += self.speed

提示：
    image 的 get_rect() 方法 可以返回 矩形对象 -- pygame.Rect(0,0,图像宽,图像高)的对象
"""

# 导入模块的顺序
# 1、官方标准模块导入
# 2、第三方模块导入
# 3、应用程序模块导入
import random
import pygame

pygame.init()

# 屏幕大小的常量
# 常量的定义
#   定义常量和定义变量的语法是完全一样的，都是使用赋值语句
#   常量的命令应该所有字母都使用大写，单词与单词使用下划线连接
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 定义刷新频率的常量
TICK = 60

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """创建游戏精灵类  指定sprite为父类"""

    def __init__(self, image_name, speed=1):
        # 调用父类__init__方法
        super().__init__()

        # 定义对象的属性Background
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    # 1、调用父类方法  实现精灵的创建
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        # 2、判断是否是交替图像，如果是  需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1、调用父类的方法实现
        super().update()
        # 2、判断图像是否移除屏幕、如果移出，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    # 在初始化中 指定敌机的图片  随机位置 随机速度
    def __init__(self):
        super().__init__("./images/enemy1.png")

        # 2、指定随机速度   1-3
        self.speed = random.randint(1, 3)

        # 3、指定随机初始位置
        # self.rect.y = -SCREEN_RECT.height
        self.rect.bottom = 0

        # 屏幕宽度-飞机的宽度
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直方向的飞行
        super().update()

        # 判断是否飞出屏幕  如果飞出  从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞机飞出屏幕...")
            self.kill()

    def __del__(self):
        pass
        # print("敌机挂了 %s" % self.rect)


# 新建英雄类
class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1、调用父类方法，设置image和speed
        super().__init__("./images/me1.png", 0)
        # 2、设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄运动边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print("biubiubiu")
        for i in (0, 1, 2):
            # 1、创建子弹精灵
            bullet = Bullet()
            # 2、设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3、将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法，让子弹沿垂直放行飞行
        # 在初始化方法中重写了父类方法 y - 2  所以子弹是向上飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
        # print("子弹销毁")
