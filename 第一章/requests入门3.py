import requests

url = "https://movie.douban.com/j/chart/top_list"

args = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}

resp = requests.get(url, params=args, headers=headers)

# print(resp.request.url)
# print(resp.request.headers)
print(resp.json())
resp.close()
