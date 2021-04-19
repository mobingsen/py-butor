from Crypto.Cipher import AES  # pip install pycrypto
from base64 import b64encode
import requests
import json


# https://music.163.com/#/song?id=1325905146
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a8" \
    "76aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6" \
    "c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d5" \
    "46b8e289dc6935b3ece0462db0a22b8e7 "
g = "0CoJUm6Qyw8W8jud"
i = "JyuZ5RAGgzZPVsiA"  # 把随机值定死为固定值


def get_encSeckey():
    return "aec6a89766242f7ddcc6ed94a5c46fb6f02da59112047260c2259629fce339e574c50" \
           "2715a46bdda5ba8849388d6ed39292f869e7ad2952d02d9598780f19d6b21bcfef5d8" \
           "d613c8a8392bdca2a6381d1e85fe504c8ee1ab9e864de0ad551a25d4267a82b9788fd" \
           "bdd2c095714509112b2d925bfd470006f4be4e40b657ab290"


def get_params(data):
    first = enc_paprams(data, g)
    second = enc_paprams(first, i)
    return second


def enc_paprams(data, key):
    aes = AES.new(key=key.encode("utf-8"), IV="0102030405060708".encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data)
    return str(b64encode(bs), "utf-8")


resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSeckey()
})

print(resp.text)