import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"

# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find("div", class_="TypeList").find_all("a")
# print(a_list)
for a in a_list:
    href = a.get('href')
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("p", align="center")
    img = p.find("img")
    src = img.get("src")
    img_resp = requests.get(src)
    # img_resp.content # 拿到的是字节
    img_name = src.split("/")[-1]
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)
    print("done..." + img_name)
    time.sleep(1)
f.close()
print("--end--")