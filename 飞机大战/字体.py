# -*- coding:utf-8 -*-
my_name = "分数"
import pygame

pygame.init()
my_font = pygame.font.SysFont("simSun", 66)
name_surface = my_font.render(u'分数', True, (0, 0, 0), (255, 255, 255))

pygame.image.save(name_surface, "name.png")

enemy_hit_dict = dict()

score = 0

ENEMY_SCORE = 100

# enemy_hit_dict = pygame.sprite.groupcollide(enemy_group, hero.bullets, True, True)
# score += len(enemy_hit_dict) * ENEMY_SCORE;  # 计算得分
# enemy_hit_group.add(enemy_hit_dict)


screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/background.png")
# 2、使用blit方法将背景绘制在屏幕的(0,0)位置
screen.blit(bg, (0, 0))
screen.blit(name_surface, (20, 20))
# 3、更新屏幕
pygame.display.update()
