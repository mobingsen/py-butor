import requests
import re
import csv

domain = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.182 Safari/537.36"
}
# verify=False去掉安全验证
resp = requests.get(domain, verify=False)
resp.encoding = 'gb2312'
# print(resp.text)

obj = re.compile(r"2020必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result = obj.finditer(resp.text)
child_href_list = []
for it in result:
    ul = it.group('ul')
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)
        # print(child_href)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie").strip())
    print(result3.group("download"))
