import re

# findall: 匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "中国移动：10086，中国电信：10010")
print(lst)
print('1-----------------')
# finditer: 匹配字符串中所有的内容【返回的是迭代器】,从迭代器中拿到数据需要.group()
it = re.finditer(r"\d+", "中国移动：10086，中国电信：10010")
for i in it:
    print(i.group())
print('2-----------------')
# search找到一个结果就返回，返回的结果是match对象，拿到数据需要.group()
s = re.search(r"\d+", "中国移动：10086，中国电信：10010")
print(s.group())
print('3-----------------')
# match是从头开始匹配
m = re.match(r"\d+", "10086，中国电信：10010")
print(m.group())

print('4-----------------')
obj = re.compile(r"\d+")
ret = obj.finditer("中国移动：10086，中国电信：10010")
for i in ret:
    print(i.group())