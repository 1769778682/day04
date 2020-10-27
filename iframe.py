# 1.导包
import time
from selenium import webdriver
# 2.创建浏览器驱动对象

driver = webdriver.Chrome()
driver.maximize_window()
# 3.打开测试网址打开注册A.html页面，完成以下操作

driver.get(
    "https://i.qq.com/")
# 4.业务操作
driver.switch_to.frame(driver.find_element_by_id("login_frame"))
time.sleep(2)
driver.find_element_by_id("switcher_plogin").click()
# 返回主页
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_css_selector(".icon_iphone").click()
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()
