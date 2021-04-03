import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)


def download_one_page(url):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # trs = table.xpath("./tr")[1:]
    trs = table.xpath("./tr[position()>1]")[1:]
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据进行简单的处理
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        csv_writer.writerow(txt)
    print("----")


if __name__ == '__main__':
    # for i in range(1, 14870):
    #     download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("----")
