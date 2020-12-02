"""
 f = open("tcp_server")
 try:
     f.write()
except:
    f.close()
 
 可以写为
 with open("xxx","wb")  as  f:                  # 以读写的方式打开文件    b 是以二进制方式写入
    f.read()/write()                  # 读取或者写入后   关闭
#这样只要可以打开文件  就可以正常关闭
"""
import socket


def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、获取服务器的IP和端口
    IP = input("请输入服务器IP：")
    PORT = int(input("请输入服务器端口："))
    # 3、连接服务器
    tcp_socket.connect((IP, PORT))

    # 4、获取下载的文件名字
    download_file_name = input("请输入要下载的文件名称：")

    # 5、将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode("gbk"))
    # 6、接收文件中的数据
    recv = tcp_socket.recv(1024)
    if recv:
        # 7、保存接收到的数据到一个文件中
        with open(download_file_name, "wb") as f:
            f.write(recv)
    else:
        print("空文件")

    recv_name = tcp_socket.recv(1024)
    print("服务器返回消息 %s " % str(recv_name.decode("gbk")))
    # 8、关闭套接字

    tcp_socket.close()


if __name__ == "__main__":
    main()
