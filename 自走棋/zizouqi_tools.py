import random

random = random.randint(1, 3)


# print(random)

# player_chouka = int(input("请输入您要武将 (1)天使/(2)卡牌/(3)剑姬："))
class Game(object):
    @staticmethod
    def show_help():
        print("(1)石头/(2)剪刀/(3)布")

    def __init__(self):
        self.num = 0
        self.big_num = 5
        self.hero_list = []
        self.chuzhan_heronum = 0
        self.big_chuzhan_heronum = 3
        self.blood = 100
        print("目前拥有武将 %d   已上阵 %d    剩余血量 %d" % (self.num, self.chuzhan_heronum, self.blood))

    def chouka(self):
        if self.big_num < self.num:
            print("您武将位置已满 请出售后购买")
        else:
            player_chouka = int(input("请输入您要武将 (1)天使/(2)卡牌/(3)剑姬："))
            if player_chouka == 1:
                self.hero_list.append("天使")
                self.num += 1
                print("您已选取【天使】    全部武将：%s" % self.hero_list)
                print(self.num)
            elif player_chouka == 2:
                self.hero_list.append("卡牌")
                self.num += 1
                print(self.num)
                print("您已选取【卡牌】    全部武将：%s" % self.hero_list)
            elif player_chouka == 3:
                self.hero_list.append("剑姬")
                self.num += 1
                print("您已选取【剑姬】    全部武将：%s" % self.hero_list)
                print(self.num)
            else:
                return

    def chuzhan(self):
        if self.big_chuzhan_heronum < self.chuzhan_heronum:
            print("上阵武将已到最大限制 请升级后上阵")
        else:
            player_chuzhan = int(input("请输入您要上阵的武将 (1)天使/(2)卡牌/(3)剑姬："))
            if player_chuzhan in self.hero_list:
                if player_chuzhan == 1:
                    self.hero_list.remove("天使")
                    self.chuzhan_heronum += 1
                    print("【天使已上阵】")
                elif player_chuzhan == 2:
                    print("%s" % self.hero_list)
                    self.hero_list.remove("卡牌")
                    self.chuzhan_heronum += 1
                    print("【卡牌已上阵】")
                elif player_chuzhan == 3:
                    self.hero_list.remove("剑姬")
                    self.chuzhan_heronum += 1
                    print("【剑姬已上阵】")
            else:
                return

    def solo(self, random, hero_1):

        if self.blood < 0:
            print("已死亡")
            exit()
            # hero_1 = int(input("请你输入技能【1-3】："))
        else:
            if (hero_1 >= 1 and hero_1 <= 3):

                #                    if random > hero_1:
                #                        print("电脑 获胜")
                if ((hero_1 == 1 and random == 2)
                        or (hero_1 == 2 and random == 3)
                        or (hero_1 == 3 and random == 1)):

                    if self.blood <= 1:
                        print("玩家 已死亡")
                    self.blood -= 1
                #               elif  random < hero_1:
                #                   print("%s  获胜" % hero_1)
                #                    if self.blood >= 100:
                #                        print("血量已满  无法增加")
                #                    self.blood += 1
                #                elif  random == hero_1:
                #                    print("此局平局   决战到天亮")
                elif hero_1 == random:
                    print("心有灵犀")
                elif hero_1 > random:
                    print("玩家  获胜")
                    if self.blood >= 100:
                        print("血量已满  无法增加")
                    self.blood += 1
            else:
                print("输入错误")
