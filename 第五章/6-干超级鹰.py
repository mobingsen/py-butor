from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")

img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰用户名的密码', '96001')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

username = '用户名'
password = ''
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(username)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(2)

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()