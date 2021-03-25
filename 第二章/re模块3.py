
import requests
import re
import csv

domain = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.182 Safari/537.36"
}
resp = requests.get(domain, verify=False) # verify=False去掉安全验证
resp.encoding='gb2312'
# print(resp.text)

obj = re.compile(r"2020必看热片.*?<ul>.*?<a href='(?P<link_addr>.*?)' title=.*?</ul>", re.S)
result = obj.finditer(resp.text)
for it in result:
    print(it.group())
