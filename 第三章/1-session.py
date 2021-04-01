import requests

session = requests.session()
data = {
    "loginName": "18614075987",
    "password": "q6035945"
}

url = "https://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)

resp2 = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp2.json())