# 迭代器
# 我们已经知道对list、tuple、str等类型的数据使用for in 的循环语法从其中依次拿到数据
# 进行使用，我们把这样的过程称为遍历，也叫迭代

# 判断是否可以迭代
from collections import Iterable

print(isinstance([1, 2, 3], Iterable))

print(isinstance(100, Iterable))

# 对象是否可以迭代
