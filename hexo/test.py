# 1、定义input_password函数，提示用户输入密码
# 2、如果用户输入长度 < 8  抛出异常
# 3、如果用户输入长度 >= 8  返回输入的密码


def input_password():
    # 1、定义input_password函数，提示用户输入密码
    pwd = input("请输入密码：")
    # 2、如果用户输入长度 < 8  抛出异常
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    raise ex


try:
    print(input_password())  # 执行函数并打印
except Exception as  result:  # 捕获所有异常 并 传递到result 变量
    print(result)
finally:  # 所有情况下都会执行的代码
    print("代码结束")
