import random

# 产生0-1的随机浮点数
print(random.random())
# 产生指定范围内的随机浮点数
print(random.uniform(1, 2))
# 产生指定范围内的随机整数
print(random.randint(5, 10))
# 从一个指定步长的集合中产生随机数
print(random.randrange(10, 30, 5))  # (从10-30 步长为5 产生随机数 10，15,20,25,30)
# 从序列中获取一个随机元素  random.choice(sequence)
# 参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
str = "test", "test2", "test3", "test4"
print(random.choice(str))

# 将一个列表中的元素打乱
list = ["a", "b", "c", "d", "e", "f", "g"]
random.shuffle(list)
print(list)

# 从序列中随机获取指定长度的片段
list = ["a", "b", "c", "d", "e", "f", "g"]
print(random.sample(list, 4))  # 打印序列中的四个
num = ["1", "2", "3", "4", "5", "6"]
print(random.sample(num, 3))  # 打印序列中的三个
