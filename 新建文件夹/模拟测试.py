print("            welcome to python        ")
count = 0
while count < 3:
    day = int(input("please input password  ："))
    print("您输入的密码是 %d " % day)
    if day == 316:
        print("密码输入正确")
        print("hello,welcome to python")

        app = eval(input("请输入要执行的程序 请把输入使用""引起来(1)QQ/(2)微信/(3)游戏: "))

        if app == "QQ":
            aa = int(input("请输入您的QQ号码: "))
            if aa == 942868591:
                mima = eval(input("请您输入密码："))
                if mima == 199800:
                    print("登录成功")
            else:
                print("请重新输入")
        elif app == "微信":
            bb = int(input("请输入您的微信号码: "))
        elif app == "游戏":

            print("get out")
        else:
            print("输入错误")
        break
    else:
        print("密码错误（提示密码是silly dog birthday）")
    count = count + 1
