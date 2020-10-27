# 1.导包
import time
from selenium import webdriver
# 2.创建浏览器驱动对象

driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作

driver.get(
    "https://www.baidu.com/")
# 4.业务操作
# print(driver.get_cookies())
time.sleep(2)
driver.add_cookie({"name": "BDUSS",
                   "value": "VUTkdwWDlqeW50UXB4b3pEb0VXUVR1aXdSfjVXbU"
                            "RwZHBFSFlFY1pvZ1JiZ2hmRVFBQUFBJCQAAAAAAA"
                            "AAAAEAAAB4U4RWU3VpeWFuZ25hbgAAAAAAAAAAAA"
                            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                            "AAAAAAAAAAAAAAAAAAABHh4F4R4eBeQj"})
driver.refresh()
# print(driver.get_cookie("testName"))
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()