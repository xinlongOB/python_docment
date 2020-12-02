# encoding: utf-8

import json

json_str = '{"name":"haha", "age":9}'  # 若定义json字符串，{}里面必须是双引号，所以{}外面是单引号
# JSON 中表示上面的字符串是object对象，还有array数组
json_array = '[{"name":"haha", "age":9, "flag":false}, {"name":"xixi", "age":8}]'
student = json.loads(json_str)
student1 = json.loads(json_array)
print(type(student1))
print(student1)
print(type(student))
print(student)
