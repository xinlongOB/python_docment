print('----------linux----------')
temp = input("请输入一个数字：")
guess = int(temp)
while guess != 9:
    temp = input("猜错了，请重新输入一个数字：")
    guess = int(temp)
    if guess == 9:
        print("对，没错恭喜您猜对了")
    elif guess > 9:
        print("接近了，但是大了些哟")
    else:
        print("接近了，但是小了些哟")
print("游戏结束")
