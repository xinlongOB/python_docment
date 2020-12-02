import cards_tools

##while  True 无限循环   由用户主动绝对什么时候退出循环
while True:
    # TODO 显示功能菜单
    ##导入tools函数
    cards_tools.login()
    action_str = input("请选择系统执行的操作 : ")
    print("您选择的操作是 【%s】 " % action_str)
    ##1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        ##新增名片
        if action_str == "1":
            cards_tools.insert()
        ##显示全部
        elif action_str == "2":
            cards_tools.show_all()
        ##查询名片
        elif action_str == "3":
            cards_tools.find()

    ## 0 退出系统
    elif action_str == "0":
        break
    ## 如果在开发过程中不希望立刻编写分支内部的代码，可以使用pass关键字，表示一个占位符，
    ## 程序运行是，pass关键字不会执行任何操作
    # pass

    ## 其他内容输入错误，需要提示用户
    else:
        print("输入错误，请重新输入")
