import socket
import re
import gevent
# 导入gevent 中的monkey库
from gevent import monkey

# 由于IO操作非常耗时，程序经常会处于等待状态
# 比如请求多个网页有时候需要等待，gevent可以自动切换协程
# 遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()解决
# 首行添加下面的语句即可
monkey.patch_all()


def service(new_socket):
    """为这个客户端返回数据"""
    # 1、接收客户端请求--即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode("utf-8")
    # print(request)

    # 将请求已列表的形式赋值并打印
    request_lines = request.splitlines()
    print(request_lines)

    # 正则匹配文件名 把需要取出的文件名用()  group()方法
    # GET /index.html HTTP/1.1
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    print(request_lines[0])
    # 判断ret 是否有值 或是个对象
    print(ret)
    if ret:
        file_name = ret.group(1)
        print("*" * 30, file_name)
        if file_name == "/":
            file_name = "./index.html"

    # 2、返回http格式的数据给浏览器
    # try 打开文件  当前路径下html目录中的文件
    try:
        f = open("./html" + file_name, "rb")
    # 如果打开失败  返回404
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----file not exist----"
        new_socket.send(response.encode("utf-8"))

    # 打开成功 读取文件内容并发送
    else:

        # 2.1 、准备发送浏览器的数据---header
        response = "HTTP/1.1 200 OK \r\n"
        response += "\r\n"

        # 2.2 、准备发送给浏览器的数据---boy
        html = f.read()
        f.close()
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html)

    # 3、 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定
    tcp_server_socket.bind(("192.168.0.114", 1100))
    # 3、变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4、等待客户端连接
        new_socket, client = tcp_server_socket.accept()

        # 5、为这个客户端服务
        gevent.spawn(service, new_socket)

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
