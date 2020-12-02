# -*- coding: utf-8 -*
import socket


def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2、绑定地址
    tcp_socket.bind(("", 1111))
    # 3、开启监听模式
    tcp_socket.listen(128)
    # 4、接收数据     accept 返回的是一个元祖  所以把返回值赋值给两个变量名
    new_client_socket, client_addr = tcp_socket.accept()
    print("一个新连接已经链接%s" % str(client_addr))
    # 接收客户端下载的文件名
    filename = new_client_socket.recv(1024).decode("gbk")
    print("客户端(%s)需要下载的文件是 ：%s" % (str(client_addr), filename))
    # 打开文件
    try:
        f = open(filename, "rb")
        data = f.read()
        f.close()
        new_client_socket.send(data.encode("gbk"))
    except Exception as ret:
        new_client_socket.send("文件不存在 404".encode("gbk"))
        print("文件不存在 404")

        # with open(filename,"r") as f:
        # data  = f.read()
        # new_client_socket.send(data.encode("gbk"))

    # 关闭套接字
    new_client_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
