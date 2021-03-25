import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.182 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)
result = obj.finditer(page_content)
f = open("data.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num"))
    # print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csv_writer.writerow(dic.values())
f.close()
print('--end--')