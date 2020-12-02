"""
英雄需求
1、游戏启动后，英雄出现在屏幕的水平中间位置，距离底部有120 像素
2、英雄每隔0.5s 发射一次子弹，每次连发三枚子弹
3、英雄默认不会移动，需要通过左右方向键，控制英雄在水平方向移动

子弹需求
1、子弹从英雄的正上方发射沿直线向上方飞行
2、飞出屏幕后，需要从精灵组中删除


Hero——英雄
初始化
    指定英雄图片
    初始速度=0  英雄默认静止不动
    定义bullets 子弹精灵组保存子弹精灵

重新update方法
    英雄需要水平移动
    并且保证不能移除屏幕
增加bullets属性，记录所有子弹精灵
增加fire方法，用于发射子弹


1、在plane_sprites新建Hero类
重新初始化方法，直接指定图片名称、并且将初始化速度设置为0

设置英雄初始位置
centerx = x + 0.5 * width     # centerx等于屏幕的x值 加上 宽度的一半     指x的中心点
bottom属性是y值       可以使用height - 120
    例如：
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120



2、绘制英雄
在_create_sprites添加英雄精灵和英雄精灵组
    后续要针对英雄做碰撞检测以及发射子弹
    所以英雄需要单独定义成属性
在_update_sprites 让英雄精灵组调用update和draw方法


3、移动英雄位置
在pygame 中 针对键盘按键的捕获 有两种方式
第一种：判断event.type == pygame.KEYDOWN       判断事件类型是否是按下键盘
第二组：
    1、首先使用pygame.key.get_pressed()返回所有按键元祖
    2、通过键盘常量，判断元祖中某一个键是否被按下，  --如果被按下，对应数值为 1

    第一种方式
    elif event.type == pygame.KEYDOWN and  envet,key == pygame.K_RIGHT:
        #判断是否按下了键盘  并且是否是按下向右的按键
        print("向右移动...")

    第二种方式
    #返回所有按键的元祖，如果某个键被按下，对应的值会是1
    keys_pressed = pygame.key.get_pressed()
    #判断是否按下了向右的方向键
    if keys_pressed[pygame.K_RIGHT]:
        print("向右移动...")

结论
    第一种方式event.type用户必须要抬起按键才算一次按键事件，操作灵活性会大打折扣
    第二种用户可以按住方向键不放，就能够实现持续向某一个方向移动了，操作灵活性更好
    #第一种就属于M16 只可以单点
    #第二种属于M1416 可以连发

3、移动英雄位置
    1、在hero类中重写update方法
        用速度speed和英雄rect.x 进行叠加
    2、在__event.handler方法中根据左右方向键设置英雄的速度
        向右 => speed = 2
        向左 => speed = -2
        其他 => speed = 0

        # 判断是否按下了向右的方向键    K_RIGHT 向右    K_LEFT 向左
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed += 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed += -2
        else:
            self.hero.speed = 0

    控制英雄运动边界
    在hero类中update()方法判断英雄是否超出屏幕边界
        right = x + widt
        利用right 属性可以非常容易的针对右侧设置精灵位置


发射子弹
回顾--英雄需求
1、游戏启动后，英雄出现在屏幕的水平中间位置，距离底部有120 像素
2、英雄每隔0.5s 发射一次子弹，每次连发三枚子弹
3、英雄默认不会移动，需要通过左右方向键，控制英雄在水平方向移动

添加发射子弹事件
pygame的定时器使用套路非常固定
1、定义定时器常量 --eventid     # HERO_FIRE_EVENT = pygame.USEREVENT + 1
2、在初始化方法中，调用set_timer方法设置定时器事件    #pygame.time.set_timer(HERO_FIRE_EVENT,500)
3、在游戏循环中，监听定时器事件


回顾--子弹需求
1、子弹从英雄的正上方发射沿直线向上方飞行
2、飞出屏幕后，需要从精灵组中删除

Bullet -- 子弹
初始化方法
    指定子弹图片
    初始速度 = -2    --子弹需要向上方飞行
重写update()方法
    判断是否飞出屏幕，如果是，从精灵组删除

详细信息
    定义子弹类
        在plane_sprites新建Bullet类继承GgameSprites
        重写初始化方法，直接指定图片名称、并且设置初始速度
        重写update()方法，判断子弹飞出屏幕 从精灵组删除

一次发射三枚子弹
    修复fire()方法  一次发射三枚子弹
     for 循环    子弹的bottom 和英雄的Y值相差 0  20  40个点
        for i in (0,1,2):
            #1、创建子弹精灵
            bullet = Bullet()
            #2、设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            #3、将精灵添加到精灵组
            self.bullets.add(bullet)


碰撞检测
pygame提供了两个非常方便的方法可以实现碰撞检测
    pygame.sprite.groupcollide(group1,group2.dokill1,dokill2,collided = None)  -> Sprite_dict
    如果将dokill 设置为True。则发生碰撞的精灵将被自动移除
    collided 参数适用于计算碰撞的回调函数
        如果没有指定，则每个精灵必须有一个rect属性
"""
