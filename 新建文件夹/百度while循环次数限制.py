import random

secret = random.randint(1, 20)
count = 1
print('---自己测试---')
temp = input('guess the number:')
guess = int(temp)
while guess != secret and count < 3:
    if guess > secret:
        print('too big')
    else:
        print('too small')
    temp = input('try again:')
    guess = int(temp)
    count = count + 1
    print(count)

if guess == secret:
    print('bingo')
    print('game over')
