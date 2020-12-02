name_list = ["张三", "李四", "王五", "赵六"]

##使用循环遍历
##循环打印列表中的数据 第一个除外
a = 0
for myname in name_list:

    a += 1
    if a == 1:
        print("错误")
        continue
    else:
        print("myname is %s" % myname)
