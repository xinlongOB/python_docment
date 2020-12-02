import random

secret = random.randint(1, 10)
print('----------linux----------')
temp = input("请输入一个数字：")
guess = int(temp)
count = 0
while guess != secret and count < 3:
    if guess > secret:
        print("接近了，但是大了些哟")
        temp = input("猜错了，请重新输入一个数字：")
        guess = int(temp)
        count += 1
    else:
        guess < secret
        print("猜小了")
        temp = input("猜错了，请重新输入一个数字：")
        guess = int(temp)
        count += 1

if guess == secret:
    print("没错恭喜您猜对了")
print("游戏结束")
