"""
pip install selenium -i 清华源
下载浏览器驱动： https://npm.taobao.org/mirrors/chromedriver
"""
from selenium.webdriver import Chrome

web = Chrome()

web.get("https://www.baidu.com")

print(web.title)