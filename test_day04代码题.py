# 1.导包
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# 2.创建浏览器驱动对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# 3.打开测试地址
driver.get('http://localhost/')
# 4.业务操作
"""--------登陆----------"""
driver.find_element_by_css_selector(".red").click()
driver.find_element_by_id('username').send_keys('15800000001')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('verify_code').send_keys('8888')
driver.find_element_by_name('sbtbutton').click()
WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath("//*[text()='安全退出']"))

driver.find_element_by_css_selector(".top-ri-header [href*='order']").click()

# 窗口切换
# time.sleep(1)
handles = driver.window_handles
driver.switch_to.window(handles[-1])

driver.find_element_by_xpath("//*[text()='地址管理']").click()
driver.find_element_by_xpath("//*[text()='增加新地址']").click()

# iframe切换
driver.switch_to.frame(driver.find_element_by_css_selector("[id*='layui-layer-iframe']"))
driver.find_element_by_css_selector(".box-ok").click()

# 获取弹出框
time.sleep(5)
driver.switch_to.alert.accept()

# ------- 新增地址-------
time.sleep(5)
customer_name = "Test{}".format(time.strftime("%H%M%S"))
WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_name("consignee")).send_keys(customer_name)
Select(driver.find_element_by_id("province")).select_by_value("1")
Select(driver.find_element_by_id("city")).select_by_value("2")
Select(driver.find_element_by_id("district")).select_by_value("14")
Select(driver.find_element_by_id("twon")).select_by_value("15")
driver.find_element_by_id("address").send_keys("test123")
driver.find_element_by_name("mobile").send_keys('15800000003')
driver.find_element_by_css_selector(".box-ok").click()
time.sleep(2)
driver.refresh()


# 判断新增地址是否成功
def is_exist(text):
    try:
        xpath_str = "//*[text()='{}']".format(text)  # //*[text()='Test094658']
        is_suc = driver.find_element_by_xpath(xpath_str)
    except Exception as e:
        is_suc = False
        # 记得导包
        NoSuchElementException("找不到文本为:{}的元素对象".format(text))
    return is_suc


if is_exist(customer_name):
    print("新增地址成功")
else:
    print("新增失败")

# 5.关闭浏览器
time.sleep(8)
driver.quit()
