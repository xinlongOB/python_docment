##石头剪刀布游戏测试
import random

random = random.randint(1, 3)
print("————python————")

##电脑出的拳
computer = random
count = 0

##比较胜负
##1 石头 胜 剪刀
##2 剪刀 胜 布
##3 布   胜 石头
##玩家胜利
while count < 3:

    player = int(input("请输入您要猜的拳 (1)石头/(2)剪刀/(3)布："))
    print("玩家选择的拳头是 %d 电脑出的拳头是 %d" % (player, computer))
    if (player == 1) or (player == 2) or (player == 3):
        if ((player == 1 and computer == 2)
                or (player == 2 and computer == 3)
                or (player == 3 and computer == 1)):

            print("恭喜玩家胜利，电脑弱爆了")

        ##平局情况
        elif player == computer:
            print("心有灵犀")

        else:
            print("不好意思，电脑胜利")

    else:
        print("输入错误")
    ##       player = int(input("请输入您要猜的拳 (1)石头/(2)剪刀/(3)布："))

    count = count + 1
