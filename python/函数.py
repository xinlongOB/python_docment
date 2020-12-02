# 定义一个函数
##def test(zifu,cishu):
##    print(zifu * cishu)
# test("-",20)


# name = "pro_hf"

# print(name)

# print("合服标识 %s" % name)
name_list = [
    {"name": "小小",
     "age": "20"},
    {"name": "yy",
     "age": "20"}
]


def test():
    for all in name_list:
        if all["name"] == "小小":
            all["name"] = find(all["name"], "请输入 ：")

    print(name_list)


def find(aa, nishi):
    re = input(nishi)
    if len(re) > 0:
        return re
    else:
        return aa


test()
