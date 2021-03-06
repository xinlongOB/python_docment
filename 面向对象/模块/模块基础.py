# 模块的概念
# 模块是python程序架构的一个核心概念
# 每一个以扩展名py结尾的python源代码文件都是一个模块
# 模块名同样也是一个标识符。需要符合标识符的命名规则
# 在模块中定义的全局变量、函数、类都是提供给外界直接使用的工具
# 模块就好比是工具包，要想使用这个工具包中的工具，就需要先导入这个模块

# 模块的导入方式
# 1、import 导入

# import 模块名1
# import 模块名2


# 提示：在导入模块时，每个导入应该独占一行

# 导入之后   通过模块名.  使用模块提供的工具--全局变量、函数、类
# TODO 案例查看import
# import  导入指定别名
# import  模块名  as  模块别名
import test_1 as  T1

T1.hello()

# 2、from ... import 局部导入
# 如果希望从某一模块中，导入部分工具，就可以使用from...import 的方式
# from  模块名  import 工具名

# 导入后  不需要通过模块名.   的方式调用

# 从test_2 模块中导入hello这个函数
from test_2 import hello

# 直接调用  不需要通过模块名.   的方式调用
hello()

# 注意：如果两个模块，存在同名的函数，那么后导入模块的函数，会覆盖先导入的函数
