"""
目标：
1、项目准备
2、使用pygame创建图形窗口
3、理解图像并实现图像绘制
4、理解游戏循环和游戏始终
5、理解精灵和精灵组

项目准备
1、新建飞机大战项目
2、新建一个pygame_入门文件
3、导入游戏素材图片

游戏的第一印象
把一些静止的图像绘制到游戏窗口中
根据用户的交互或其他情况、移动这些图像、产生动画效果
根据图像之间是否发生重叠，判断敌机是否被摧毁等其他情况

"""

# 使用python创建图形窗口
# 1、游戏的初始化和退出
# 2、理解游戏中的坐标系
# 3、创建游戏主窗口
# 4、简单的游戏循环
#       可以将图片素材绘制到游戏的窗口上，开发游戏之前需要先知道如何建立游戏窗口

# 1.1 游戏的初始化和退出
# 要使用pygame提供的所有功能之前   需要调用init()方法
# pygame.init() 导入并初始化所有pygame模块，使用其他模块之前，必须先调用init方法
# 游戏结束前需要调用一下quit()方法
# pygame.quit() 卸载所有pygame模块， 在游戏结束之前调用

# 例如：
# -*- coding:utf-8 -*-
import pygame

pygame.init()

print("游戏代码")

pygame.quit()

"""
游戏中的坐标系
坐标系
    原点在左上角(0.0)
    x轴水平方向向右，逐渐增加
    y轴垂直方向向下，逐渐增加
    
在游戏中，所有可见的元素 都是以 矩形区域 来描述位置的
    要描述一个矩形区域有四个要素：(x,y)(width,height)
    pygame专门提供了一个类pygame.Rect 用于描述矩形区域
    Rect(x,y,width,height) - > Rect
    
提示：pygame.Rect 是一个比较特殊的类，内部只是封装了一些数字计算
    不执行pygame.init()方法同样能够直接使用
    pygame.Rect  所有参数： x，y     （坐标值）
                        left,top,bottom,right
                        center,centerx,centery
                        size,width,height     (size是一个元祖，返回的一个参数是width，第二个参数是height）
                    


#需求
#1、定义hero_rect矩形描述英雄的位置和大小
#2、输出英雄的坐标原点(x 和 y)
#3、输出英雄的尺寸(宽度和高度)
hero_rect = pygame.Rect(100,500,120,150)
print("英雄的原点 %d %d"  % (hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d  %d " % (hero_rect.width,hero_rect.height))
#英雄的宽度可以使用size输出
print("英雄的尺寸 %d  %d " % (hero_rect.size))
"""
"""
创建游戏主窗口
pygame专门提供了一个模块pygame.display  用于创建和管理游戏窗口
方法：pygame.display.set_mode()            pygame.display.update()
说明：初始化游戏显示窗口                    刷新屏幕内容显示

set_mode方法
 set_mode(resoultion=(0,0),flags=0,depth=0)  ->surface 
           等号后面指的是缺省参数    可以不指定
 作用： 创建游戏显示窗口
 参数：
        resolution指定屏幕的宽 和 高，默认创建的窗口和屏幕大小一致
        flags 参数指定屏幕的附加选择，例如是否全屏等等，默认不需要传递
        depth 参数表示颜色的位数，默认自动匹配     （32位，16位，64位)
 返回值
        暂时可以理解为游戏的屏幕，游戏的元素都需要被绘制到游戏的屏幕上
注意：必须使用变量记录set_mode方法的返回结果，  因为：后续所有的图像绘制都是基于这个返回结果

#创建游戏住窗口
pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((400,800))

pygame.quit()   #退出模块

"""

"""
简单的游戏循环



pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((400,800))

while True:
    pass

pygame.quit()   #退出模块
"""

"""
理解图像并实现图像绘制
    在游戏中，能够看到的游戏元素大多都是图像
        图像文件初始是保存在磁盘上的，如果需要使用，第一波就需要被加载到内存
    要屏幕上看到某一个图像的内容，需要按照三个步骤：
    1、使用pygame.image.load()加载图像的数据
    2、使用游戏屏幕对象调用blit 方法，将图像绘制到指定位置
    3、调用pygame.display.update()方法，更新整个屏幕的显示
提示：要想在屏幕上看到绘制的结果，就一定要调用pygame.display.update()方法


#代码演练 --绘制背景图像
#需求
#1、加载background.png创建背景
#2、将背景绘制在屏幕的(0,0)位置
#3、调用屏幕更新显示背景图像

pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480,700))

#创建背景图像
#1、加载图片
bg = pygame.image.load("./images/background.png")
#2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg,(0,0))
#3、更新屏幕
pygame.display.update()

while True:
    pass

pygame.quit()   #退出模块
"""
"""
#代码演练 --绘制英雄图像
#需求：
#1、加载me1.png 创建英雄飞机
#2、将英雄飞机绘制在屏幕的(200,500)位置
#3、调用屏幕更新显示飞机图像
pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480,700))

#创建背景图像
#1、加载图片
bg = pygame.image.load("./images/background.png")
#2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg,(0,0))
#3、更新屏幕
pygame.display.update()


#创建英雄飞机
#1、加载图像
hero = pygame.image.load("./images/me1.png")
#2、绘制在屏幕
screen.blit(hero,(200,500))
#3、更新显示
pygame.display.update()


while True:
    pass

pygame.quit()   #退出模块
"""
"""
update方法的作用
    可以在screen对象完成所以的blit方法之后，统一调用一次display.update方法
    同样可以在屏幕上看到最终的绘制结果
    
    使用display.set_mode()创建的screen对象是一个内存中的屏幕数据对象
        可以理解成是 油画的 画布
    screen.blit 方法可以在 画布上绘制很多图像
        例如：英雄、敌机、子弹
        这些图像有可能会彼此的重叠或者覆盖
        display.update会将画布最终的结果绘制在屏幕上，这样可以提高屏幕绘制效率，增加游戏的流畅度
    

"""

# 理解游戏循环和游戏时钟
"""
    游戏中的动画实现原理
        跟电影的原理类似，游戏中的动画效果，本质上是快速的在屏幕上绘制图像
         电影是将多张静止的电影胶片连续、快速的播放，产生连贯的视觉效果
    一般在电脑上每秒绘制60次，就能够达到非常连续 高品质的动画效果
        每次绘制的结果称为 帧 Frame

"""

"""
游戏的两个组成部分
    游戏初始化
            设置游戏窗口-->绘制图像初始位置-->设置游戏时钟
    游戏循环
            设置刷新帧率-->检测用户交互-->更新所有图像位置-->更新屏幕显示

游戏循环的作用
1、保证游戏不会直接退出
2、变化图像位置 -- 动画效果
    每隔1/60秒移动一下所有图像的位置
    调用pygame.display.update()更新屏幕显示    
3、检测用户交互 -- 按键、鼠标等
"""

"""
游戏时钟
    pygame专门提供了一个类pygame.time.Clock可以非常方便的设置屏幕绘制速度 --刷新帧率
    要使用时钟对象需要两部：
        在游戏初始化创建一个时钟对象
        在游戏循环中让时钟对象调用tick(帧率)方法
    tick方法会根据上次被调用的时间，自动设置游戏循环中的延时
    

pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480,700))

#创建背景图像
#1、加载图片
bg = pygame.image.load("./images/background.png")
#2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg,(0,0))
#3、更新屏幕
pygame.display.update()


#创建英雄飞机
#1、加载图像
hero = pygame.image.load("./images/me1.png")
#2、绘制在屏幕
screen.blit(hero,(200,500))
#3、更新显示
pygame.display.update()


n = 0
#使用pygame.time.Clock类创建一个时钟对象
time = pygame.time.Clock()
while True:
    #让时钟对象调用tick(帧率)方法     每秒60帧
    time.tick(60)
    print(n)

    n += 1


pygame.quit()   #退出模块
"""

# 更新英雄位置
"""
需求
1、在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置
2、在游戏循环中每次让英雄的y -1   --向上移动
3、y <= 0  将英雄移动到屏幕的底部
    
    提示：每次调用update()方法之前，需要把所有的游戏图像都重新绘制一遍
        而且应该最先重新绘制背景图像

pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480,700))

#创建背景图像
#1、加载图片
bg = pygame.image.load("./images/background.png")
#2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg,(0,0))
#3、更新屏幕
pygame.display.update()


#创建英雄飞机
#1、加载图像
hero = pygame.image.load("./images/me1.png")
#2、绘制在屏幕
screen.blit(hero,(200,500))
#3、更新显示
pygame.display.update()



#使用pygame.time.Clock类创建一个时钟对象
time = pygame.time.Clock()


#1、创建变量记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)
while True:
    #让时钟对象调用tick(帧率)方法     每秒60帧
    time.tick(60)
    #2、修改飞机的位置
    hero_rect.y -= 1

    #判断 英雄的Y值是否小于等于0
    if hero_rect.y < -200:
        hero_rect.y = 700


    #3、调用blit方法绘制图像
    screen.blit(bg,(0,0))      #如果不重新绘制背景图像    就会留下之前的残影

    screen.blit(hero,hero_rect)    #绘制英雄的图像   hero是英雄的飞机   hero_rect是之前记录的大小
    #4、更新显示
    pygame.display.update()


pygame.quit()   #退出模块

"""

# 在游戏循环中 监听事件    并且退出游戏
"""
事件event
    就是游戏启动后，用户针对游戏所做的操作
    例如：点击关闭按钮、点击鼠标、按下键盘等
    
监听
    在游戏循环中，判断用户具体的操作
    只有捕获到用户的具体操作，才能有针对性的做出响应
    
代码实现
    pygame中通过pygame.event.get()可以获得用户当前所做动作的事件列表
        用户可以同一时间做很多事  
    提示：这段代码非常的固定，几乎所有的pygame游戏都大同小异
    

pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480,700))

#创建背景图像
#1、加载图片
bg = pygame.image.load("./images/background.png")
#2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg,(0,0))
#3、更新屏幕
pygame.display.update()
#创建英雄飞机
#1、加载图像
hero = pygame.image.load("./images/me1.png")
#2、绘制在屏幕
screen.blit(hero,(200,500))
#3、更新显示
pygame.display.update()

#使用pygame.time.Clock类创建一个时钟对象
time = pygame.time.Clock()


#1、创建变量记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)
while True:
    #让时钟对象调用tick(帧率)方法     每秒60帧
    time.tick(60)

    #捕捉监听
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    #2、修改飞机的位置
    hero_rect.y -= 1

    #判断 英雄的Y值是否小于等于0
    if hero_rect.y < -200:
        hero_rect.y = 700

    #3、调用blit方法绘制图像
    screen.blit(bg,(0,0))      #如果不重新绘制背景图像    就会留下之前的残影

    screen.blit(hero,hero_rect)    #绘制英雄的图像   hero是英雄的飞机   hero_rect是之前记录的大小
    #4、更新显示
    pygame.display.update()

pygame.quit()   #退出模块
"""
# 退出游戏
"""
提示：这段代码非常的固定，几乎所有的pygame游戏都大同小异

pygame.init()     #调用模块钱需要初始化

#创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480,700))

#创建背景图像
#1、加载图片
bg = pygame.image.load("./images/background.png")
#2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg,(0,0))
#3、更新屏幕
pygame.display.update()
#创建英雄飞机
#1、加载图像
hero = pygame.image.load("./images/me1.png")
#2、绘制在屏幕
screen.blit(hero,(200,500))
#3、更新显示
pygame.display.update()

#使用pygame.time.Clock类创建一个时钟对象
time = pygame.time.Clock()

#1、创建变量记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)
while True:
    #让时钟对象调用tick(帧率)方法     每秒60帧
    time.tick(60)
    #监听退出事件
    #循环遍历 玩家的操作
    for event in   pygame.event.get():
        #判断  玩家的操作类型是否是退出事件
        if  event.type  ==  pygame.QUIT:
            print(event.type)
            print(pygame.QUIT)
            #如果是  打印 游戏退出
            print("游戏退出")
            #调用  pygame.quit()   卸载所有模块
            pygame.quit()
            # exit()   退出当前程序
            exit()

    #2、修改飞机的位置
    hero_rect.y -= 1

    #判断 英雄的Y值是否小于等于0
    if hero_rect.y < -200:
        hero_rect.y = 700

    #3、调用blit方法绘制图像
    screen.blit(bg,(0,0))      #如果不重新绘制背景图像    就会留下之前的残影

    screen.blit(hero,hero_rect)    #绘制英雄的图像   hero是英雄的飞机   hero_rect是之前记录的大小
    #4、更新显示
    pygame.display.update()

pygame.quit()   #退出模块
"""
# 精灵和精灵组
"""
精灵和精灵组
    在之前完成的案列中，图像加载、位置变化、绘制图像都需要程序员编写代码分别处理
    为了简化开发步骤。pygame提供了两个类
        pygame.sprite.Sprite  --存储图像数据image 和位置rect的对象
        pygame.sprite.Group  
        
    精灵方法：image 记录图像数据
          rect  记录在屏幕上的位置
         update(*args) ：更新精灵位置
         
    精灵组方法：
            __init__(self,*精灵)
            add(*sprites)：向组中添加精灵
            sprites()：返回所有精灵列表
            update(*args)：让组中所有精灵调用update方法
            draw(Surface)：将组中所有的image 绘制到Surface的rect位置
        如果希望在屏幕上看到最终的结果 需要调用 pygame.display.update()
"""

# 派生精灵子类
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

import pygame
class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,rect,speed):
        #调用父类__init__方法
        super.__init__()

        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        #在屏幕的垂直方向移动
        self.rect.y += self.speed
"""

# 使用游戏精灵和精灵组创建敌机
"""
需求：使用刚刚派生的游戏精灵和精灵组创建敌机并且实现敌机动画

步骤：使用from 导入 plane_sprites模块
          from导入的模块可以直接使用
          import导入的模块需要用过模块名.的方式调用
      在游戏初始化创建精灵对象 和精灵对象组
      在游戏循环中 让精灵组分别调用update()和draw（主界面）方法
      
职责：
    精灵
        封装图像image、位置rect和速度speed
        提供update方法，根据游戏需求，更新位置rect
        
    精灵组
        包含多个精灵对象
        update方法，让精灵组中的所有精灵调用 update 方法更新位置
        draw(screen)方法，在screen上绘制精灵组中所有的精灵
        
"""
from plane_sprites import *

pygame.init()  # 调用模块前需要初始化

# 创建游戏主窗口  高度和宽度默认  screen接收返回结果       执行方法：在ubuntu上python3  *.py
#                                                          不可以在pycharm上执行
screen = pygame.display.set_mode((480, 700))

# 创建背景图像
# 1、加载图片
bg = pygame.image.load("./images/background.png")
# 2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg, (0, 0))
# 3、更新屏幕
pygame.display.update()
# 创建英雄飞机
# 1、加载图像
hero = pygame.image.load("./images/me1.png")
# 2、绘制在屏幕
screen.blit(hero, (200, 500))
# 3、更新显示
pygame.display.update()

# 使用pygame.time.Clock类创建一个时钟对象
time = pygame.time.Clock()

# 1、创建变量记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建精灵对象
enemy = GameSprite("./images/enemy1.png")

enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    # 让时钟对象调用tick(帧率)方法     每秒60帧
    time.tick(60)
    # 监听退出事件
    # 循环遍历 玩家的操作
    for event in pygame.event.get():
        # 判断  玩家的操作类型是否是退出事件
        if event.type == pygame.QUIT:
            # 如果是  打印 游戏退出
            print("游戏退出")
            # 调用  pygame.quit()   卸载所有模块
            pygame.quit()
            # exit()   退出当前程序
            exit()

    # 2、修改飞机的位置
    hero_rect.y -= 1

    # 判断 英雄的Y值是否小于等于0
    if hero_rect.y < -200:
        hero_rect.y = 700

    # 3、调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 如果不重新绘制背景图像    就会留下之前的残影
    screen.blit(hero, hero_rect)  # 绘制英雄的图像   hero是英雄的飞机   hero_rect是之前记录的大小

    # 让精灵组调用两个方法    update    drwa
    # update   - 让组中的所有精灵更新位置
    enemy_group.update()

    # draw  - 在screen上绘制所有精灵
    enemy_group.draw(screen)

    # 4、更新显示
    pygame.display.update()

pygame.quit()  # 退出模块
