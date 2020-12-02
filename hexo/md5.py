import hashlib

str = "test"
str1 = hashlib.md5()
str1.update(str.encode("utf-8"))
print(str1.hexdigest())
print(str1.digest())
