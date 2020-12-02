# import requests
# import re
# url = "https://baijiahao.baidu.com/s?id=1674227391710427168&wfr=spider&for=pc"
# res = requests.get(url)
# txt = re.findall("[\u4e00-\u9fa5]{1,1000}",str(res.text))
# txt1 = "".join(txt)
# txt2 = txt1.encode()
# with open("../txt.txt","wb") as f:
#     f.write(txt2)


# import requests
# import re
# url = "https://baijiahao.baidu.com/s?id=1674227391710427168&wfr=spider&for=pc"
# res = requests.get(url)
# print(res.content)

# a = ["4","5","1","9"]
# a.remove("5")
# print(a)

num = float(input("请输入金额："))
discount = float(input("请输入折扣："))


def shop(num, disocunt):
    last = num * discount
    return last


money = shop(num, discount)
print("打折后的价格是：%f" % money)
