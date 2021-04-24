from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

# # 定位到下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下拉菜单
# sel = Select(sel_el)
#
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]/table')
#     print(table.text)
#     print('=======================================================')
#
# print("----------------------------")
# web.close()

time.sleep(5)
print(web.page_source)