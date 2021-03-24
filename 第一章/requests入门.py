# 安装requests
# pip install requests
# 清华大学开源软件镜像站 https://mirrors.tuna.tsinghua.edu.cn/
import requests

url = 'https://www.sogou.com/web?query=周杰伦'
dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
resp = requests.get(url, headers = dic)

print(resp)
# 拿到页面代码
print(resp.text)
