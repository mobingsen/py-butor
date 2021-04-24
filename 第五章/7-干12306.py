from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from chaojiying import Chaojiying_Client
import time

chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰用户名的密码', '96001')

# window.navigator.webdriver
# chrome 的版本号小于88 看1619241217(1).jpg

# chrome 的版本号大于88
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)

web.get("https://kyfw.12306.cn/otn/resources/login.html")

time.sleep(2)
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(3)

verify_img_element = web.find_element_by_xpath('//*[@id="J-loginImg"]')

dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
result = dic['pic_str'] # x1,y1|x2,y2|x3,y3
# print(result)
rs_list = result.split("|")
for rs in rs_list:
    p_temp = rs.split(",")
    x = int(p_temp[0])
    y = int(p_temp[1])
    ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform()

time.sleep(1)
username = ''
password = ''
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys(username)
web.find_element_by_xpath('//*[@id="J-password"]').send_keys(password)

web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)

btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
