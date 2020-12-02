from distutils.core import setup

setup(name="mihua",  # 包名
      version="1.0",  # 版本
      description="",  # 描述信息
      long_description="",  # 完整描述信息
      author="",  # 作者
      author_email="",  # 作者邮箱
      url="www.mihuahudong.com",  # 主页
      py_modules=["mihua_long.sendmessage",
                  "mihua_long.receivemessage"])
# py_modules  后面指定需要发布的模块
