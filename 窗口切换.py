# 1.导包
import time
from selenium import webdriver
# 2.创建浏览器驱动对象

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# 3.打开测试网址打开注册A.html页面，完成以下操作

driver.get("file:///C:/Users/sandysong/Desktop/pagetest"
           "/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
# 4.业务操作
driver.find_element_by_partial_link_text("访问").click()
han = driver.window_handles
print(han)
driver.switch_to.window(han[-1])
print(driver.current_window_handle)
time.sleep(5)
driver.find_element_by_css_selector(".inp-txt").click()
time.sleep(1)
driver.find_element_by_css_selector(".inp-txt").send_keys("传智播客")
driver.get_screenshot_as_file("./img/test.png")
driver.find_element_by_name("SearchSubButton").click()
# 5.3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()
