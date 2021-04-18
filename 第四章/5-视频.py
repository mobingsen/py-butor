import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 "
                  "Safari/537.36 "
}

# obj = re.compile(r"url: '(?P<url>.*?)',", re.S)
#
# url = "https://www.91kanju.com/vod-play/54812-1-1.html"
#
# resp = requests.get(url, headers=headers)
# m3u8_url = obj.search(resp.text).group("url")
#
# # print(m3u8_url)
# resp.close()
#
# resp2 = requests.get(m3u8_url, headers=headers)
#
# with open("哲仁王后.m3u8", mode="wb") as f:
#     f.write(resp2.content)
#
# resp2.close()
# print("--over--")

n = 1
with open("哲仁王后.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        print(line)
        resp3 = requests.get(line)
        f = open(f"video/{n}.ts", mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n += 1
