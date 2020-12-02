import socket
import re

"""
本节知识点  ：response_fail_header += "Content-Length:%d \r\n" % len(response_fail_body)

"Content-Length:%d \r\n" % len(response)
这个可以告诉浏览器body的长度  全部接受完成之后浏览器会主动断开连接
从而实现长连接
"""


def service(new_socket, request):
    """为这个客户端返回数据"""

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
        response_fail_body = "----file not exist----"
        response_fail_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_fail_header += "Content-Length:%d \r\n" % len(response_fail_body)
        response_fail_header += "\r\n"

        response_fail = response_fail_header.encode("utf-8") + response_fail_body.encode("utf-8")
        new_socket.send(response_fail)

    # 打开成功 读取文件内容并发送
    else:
        # 2.1 、准备发送给浏览器的数据---boy
        html = f.read()
        f.close()
        response_body = html

        # 2.2 、准备发送浏览器的数据---header
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content-Length:%d \r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定
    tcp_server_socket.bind(("192.168.0.114", 1100))
    # 3、变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 设置套接字为非堵塞

    client_list = list()
    while True:
        # 4、等待客户端连接
        try:
            new_socket, client = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)  # 设置套接字为非堵塞
            client_list.append(new_socket)

        for c_list in client_list:
            try:
                recv_date = c_list.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_date:
                    service(c_list, recv_date)
                else:
                    c_list.close()
                    client_list.remove(c_list)


if __name__ == "__main__":
    main()
