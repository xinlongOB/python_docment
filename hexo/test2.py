import datetime
import time

# datetime.date
localtime = datetime.date.today()  # 获取当前时间
print(localtime.strftime("%Y-%m-%d"))  # 打印当前时间的年月日
print(localtime.fromtimestamp(1592681600))  # 打印时间戳的年月日
print(localtime.isoweekday())  # 查看今天周几    周一为1
print(localtime.weekday())  # 查看今天周几  周一为0
print(localtime.isocalendar())  # 以元祖格式显示 年  第几周   周几
print(localtime.isoformat())  # 打印当前时间的年月日

# datetime.datetime
d_localtime = datetime.datetime.now()  # 获取当前时间
print(d_localtime)  # 打印当前时间(包含微秒)
print(d_localtime.year, "-", d_localtime.month, "-", d_localtime.day)  # 打印年月日
print(d_localtime.hour, ":", d_localtime.minute, ":", d_localtime.second)  # 打印时分秒
print(datetime.datetime.utcnow())  # 打印零时区的当前时间
print(d_localtime.strptime("2020-10-01 10:10:10", "%Y-%m-%d %H:%M:%S"))  # 打印自定义时间
print(d_localtime.strftime("%H:%M:%S"))  # 打印自定义格式
print(d_localtime.timetuple())  # 以元祖格式显示

# time
now = aa = (2020, 6, 19, 19, 15, 6, 4, 171, -1)  # 定义时间元祖
print(time.mktime(now))  # 元祖转换为时间戳
print(time.time())  # 打印当前时间戳
print(time.localtime())  # 打印当前时间 以元祖的格式
print(time.gmtime())  # 打印零时区的时间   以元祖的格式
