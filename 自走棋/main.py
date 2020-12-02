import zizouqi_tools
import random

# print(computer)
player = zizouqi_tools.Game()
num = 0
"""
while num < 3:

    player.chouka()
    num += 1

player.chuzhan()
"""
num2 = 0
# while num2 < 1:
#    hero_1 = int(input("请你输入技能【1-3】："))
#    player.pk(computer,hero_1)
while num2 < 1:
    computer = random.randint(1, 3)
    hero_1 = int(input("请你输入技能(1)石头/(2)剪刀/(3)布【1-3】:"))
    print(computer)
    player.solo(computer, hero_1)
