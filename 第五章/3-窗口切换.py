from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

web = Chrome()

web.get("http://lagou.com")

web.find_element_by_xpath('//*[@id="cboxClose"]').click()

time.sleep(1)
