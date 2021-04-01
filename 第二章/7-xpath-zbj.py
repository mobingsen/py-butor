import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
# print(resp.text)

html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")
for div in divs:
    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a/div[2]/div[2]/p/text()"))
    comName = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
    print(price, title, comName, location)