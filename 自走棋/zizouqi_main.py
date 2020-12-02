import random
import pygame

pygame.init()
from plane_sprites import *
import pyautogui


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))

        self.__create_sprites()

    def __create_sprites(self):
        # 1、创建背景精灵和精灵组
        bg1 = Background()
        # 第二张为交替图像  所以指定为True
        bg2 = Background(False)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        enemy = Enemy()
        # 将敌机精灵添加到精灵组
        self.enemy_group.add(enemy)
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            self.__shubioa()
            self.__event_handler()
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()

    def __shubioa(self):
        pass
        # pyautogui.moveTo()
        # print(pyautogui.position())

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断用户是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
