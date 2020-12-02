"""
socket简称套接字  是进程通信的一种方式，它与其他进程间通信的一个主要的不同是：
    它能实现主机间的进程间通信，我们网络上各种各样的服务大多都是基于socket来通信的

创建socket
在python中 使用socket模块的函数socket就可以完成
import socket
socket.socket(AddressFamily,Tyep)

说明：
    函数socket.socket创建一个socket  改函数带有两个参数
    Address Family：可以选择AF_INET(用于Internet进程间通信)，或者AF_UNIX(用于同一台进程间通信)，实际工作中常用AF_INET
    Type：套接字类型，可以是SOCK_STREAM(流式套接字，主要用于TCP协议)或者 SOCK_DGRAM(数据报套接字：主要用于UDP协议)

"""
# 创建一个tcp socket(TCP 套接字)
import socket

# 创建tcp的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ...这里是使用套接字的功能（忽略）

# 不用的时候，关闭套接字
s.close()

# 创建一个udp socket（udp 套接字）
import socket

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ...这里是使用套接字的功能（忽略）

# 不用的时候，关闭套接字
s.close()

# 套接字使用流程与文件的使用流程很相似
# 创建套接字
# 使用套接字收/发数据
# 关闭套接字
