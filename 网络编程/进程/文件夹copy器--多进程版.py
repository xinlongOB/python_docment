import os
import multiprocessing


def copy(name, old_dir, new_dir):
    """copy文件"""
    f = open(old_dir + "/" + name, "rb")
    data = f.read()
    print(data)
    f.close()

    f2 = open(new_dir + "/" + name, "wb")
    f2.write(data)
    f2.close()


def main():
    # 1 获取需要copy的文件夹的名称
    old_dir = input("请输入需要copy的文件夹名称：")

    # 2 创建新的文件夹
    try:
        new_dir_name = old_dir + "[附件]"
        os.mkdir(new_dir_name)
    except:
        pass

    # 3 获取需要copy的文件夹中所有的文件名称     listdir()
    all_files = os.listdir(old_dir)
    print(all_files)
    # 4 创建进程池
    po = multiprocessing.Pool(5)

    # 5 向进程迟中添加copy文件的任务
    for name in all_files:
        po.apply_async(copy, args=(name, old_dir, new_dir_name))

    po.close()
    po.join()


if __name__ == "__main__":
    main()
