card_list = []


def login():
    print("-" * 50)
    print("欢迎使用【名片管理系统】")
    #  print("---------------------------------------------        ")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    #  print("---------------------------------------------          ")
    print("0.退出系统")
    print("-" * 50)


def insert():
    """新增名片"""
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name = input("请输入姓名 ：")
    phone = input("请输入电话 ：")
    qq = input("请输入QQ ： ")
    email = input("请输入邮箱 :")
    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {
        "姓名": name,
        "电话": phone,
        "QQ号码": qq,
        "邮箱": email
    }

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户输入成功
    print("添加 %s 的名片成功" % name)


def show_all():
    """显示所有名片"""
    print("显示所有名片")
    # 打印表头
    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请先添加后查看")
        ##return可以返回一个函数的执行结果，不会执行下面的代码
        ##如果return后面没有任何内容，表示会返回到调用函数的位置
        ##并且不会返回任何结果
        return
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)

    # 循环遍历所有名片
    for list in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (list["姓名"],
                                            list["电话"],
                                            list["QQ号码"],
                                            list["邮箱"]))


def find():
    """搜索名片"""
    print("搜索名片")
    user = input("请输入需要查找的名片 ：")
    for findall in card_list:
        if findall["姓名"] == user:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (findall["姓名"],
                                                findall["电话"],
                                                findall["QQ号码"],
                                                findall["邮箱"]))
            two = input("请输入想执行的操作  [1]修改 [2]删除 [0]返回上一级目录  ：")
            if two == "0":
                break
            elif two == "1":
                findall["姓名"] = input_card_info(findall["姓名"], "请输入修改后的名字: ")
                findall["电话"] = input_card_info(findall["姓名"], "请输入修改后的电话: ")
                findall["QQ号码"] = input_card_info(findall["姓名"], "请输入修改后的QQ: ")
                findall["邮箱"] = input_card_info(findall["姓名"], "请输入修改后的email: ")
                print("修改完成")
            elif two == "2":
                card_list.remove(findall)
                print("%s  已删除" % user)

            else:
                break
            break
    else:
        print("%s 用户不存在" % user)


def input_card_info(former, new):
    """输入名片信息
    :param former:字典中原有的值
    :param new:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则的话返回原来的值
    """
    shuru = input(new)
    if len(shuru) > 0:
        return shuru
    else:
        return former
