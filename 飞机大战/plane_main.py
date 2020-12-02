# 导入pygame模块

import pygame
# 导入sprite的工具模块
from plane_sprites import *


class PlaneGame(object):
    """ 飞机大战主游戏"""

    def __init__(self):

        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))

        # 创建游戏的时钟
        self.clock = pygame.time.Clock()

        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 设置定时器事件  -创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

        # 设置定时器事件 -发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 1、创建背景精灵和精灵组
        bg1 = Background()
        # 第二张为交替图像  所以指定为True
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()

        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            # 1、 让时钟对象调用tick(帧率)方法     每秒60帧
            self.clock.tick(TICK)
            # 2、 监听退出事件
            self.__event_handler()

            # 3、碰撞检测
            self.__check_collide()

            # 4、更新绘制精灵组
            self.__update_sprites()

            # 5、更新显示
            pygame.display.update()

    # 2、 监听退出事件
    def __event_handler(self):
        for event in pygame.event.get():
            # 判断用户是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:

                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
                # print("敌机出场...")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 返回所有按键的元祖，如果某个键被按下，对应的值会是1
        keys_pressed = pygame.key.get_pressed()
        # 判断是否按下了向右的方向键
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed += 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed += -2
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):

        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # print("摧毁敌机")
        if pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True):
            self.hero.kill()
            PlaneGame.__game_over()
            print("英雄死亡")

    # 更新绘制精灵组
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 退出游戏
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
