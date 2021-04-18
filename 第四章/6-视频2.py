import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES  # pycryptodome
import os


def get_iframe_src(url):
    # resp = requests.get(url)
    # main_page = BeautifulSoup(resp.text, "html.parser")
    # src = main_page.find("iframe").get("src")
    # print(src)
    # return src
    return "https://boba.52kuyun.com/share/xfPs9NPHvYGhNzFp"


def get_first_m3u8_url(url):
    resp = requests.get(url)
    # print(resp.text)
    obj = re.compile(r'var main = "(?P<m3u8_url>.*?)"', re.S)
    m3u8_url = obj.search(resp.text).group("m3u8_url")
    # print(m3u8_url)
    return m3u8_url


def download_m3u8_file(url, name):
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)


async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video2/{name}", mode="wb") as f:
            await f.write(await resp.content.read())
    print(f"{name}下载完毕")


async def aio_download(up_url):
    tasks = []
    async with aiohttp.ClientSession as session:
        async with open("越狱第一季第一集——second_m3u8.txt", mode="r", encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()
                ts_url = up_url + line
                task = asyncio.create_task(download_ts(ts_url, line, session))
                tasks.append(task)

            await asyncio.wait(tasks)


def get_key(url):
    resp = requests.get(url)
    # print(resp.text)
    return resp.text


async def dec_ts(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video2/{name}", mode="r") as f1, \
            aiofiles.open(f"video2/temp_{name}", mode="wb") as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
    print(f"{name}处理完毕")


async def aio_dec(key):
    tasks = []
    async with open("越狱第一季第一集——second_m3u8.txt", mode="r") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            task = asyncio.create_task(dec_ts(line, key))
            tasks.append(task)
        await asyncio.wait(tasks)


def merge_ts():
    # mac: cat 1.ts 2.ts ... > xxx.mp4
    # windows: copy /b 1.ts+2.ts+... xxx.mp4
    lst = []
    with open("越狱第一季第一集——second_m3u8.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            lst.append(f"video2/temp_{line}")
    s = " ".join(lst)
    os.system(f"cat {s} > movie.mp4")
    print("---搞完了---")


def main(url):
    iframe_src = get_iframe_src(url)
    first_m3u8_url = get_first_m3u8_url(iframe_src)
    iframe_domain = iframe_src.split("/share")[0]
    first_m3u8_url = iframe_domain + first_m3u8_url
    # print(first_m3u8_url)
    download_m3u8_file(first_m3u8_url, "越狱第一季第一集——first_m3u8.txt")
    with open("越狱第一季第一集——first_m3u8.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()
                second_m3u8_url = first_m3u8_url.split("index.m3u8")[0] + line
                download_m3u8_file(second_m3u8_url, "越狱第一季第一集——second_m3u8.txt")
                print("---2---")
    second_m3u8_url_up = second_m3u8_url.replace("index.m3u8", "")
    asyncio.run(aio_download(second_m3u8_url_up))

    key_url = second_m3u8_url_up + "key.key"
    key = get_key(key_url)

    asyncio.run(aio_dec(key))

    merge_ts()


if __name__ == '__main__':
    url = "https://www.91kanju.com/vod-play/541-2-1.html"

    main(url)
