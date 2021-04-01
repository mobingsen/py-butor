import requests

proxies = {
    "https": "https://218.60.8.83:3129"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)