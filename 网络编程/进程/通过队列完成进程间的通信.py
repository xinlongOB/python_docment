# 队列 Queue
# q = multiprocessing.Queue()    # ()可指定参数    最多接收几条消息
# q.put  # 往队列里面放数据       数据类型任意
# q.full()  判断队列是否满了   如果满了 返回True   否则 返回false
# q.empty()  判断是否为空    如果为空 返回True   否则 返回false
# q.get   取数据  如果数据取完  则会堵塞          取出的第一个为放入的第一个数据
# q.get_nowait  取数据  如果数据取完  抛出异常   取出的第一个为放入的第一个数据
import multiprocessing
import time


def download(q):
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)  # for循环将数据放到队列中

        print("下载器已经下载完数据并且存入到队列中")
        time.sleep(1)


def analysis_data(q):
    # 数据处理
    # 从队列中获取数据
    waiting = list()  # 创建个空列表   可以直接写list()  和 waiting = []  一样
    while True:
        data = q.get()  # 循环取出数据
        waiting.append(data)  # 把取出的数据写入到列表waiting中
        print(data)
        time.sleep(1)

        if q.empty():  # 判断  如果队列为空   退出循环
            break


def main():
    # 1、创建一个队列
    q = multiprocessing.Queue()
    # 2、创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
