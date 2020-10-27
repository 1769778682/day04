# 导包
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://localhost/")
"""--->1.登陆tpshop"""
driver.find_element_by_css_selector(".red").click()
time.sleep(1)
driver.find_element_by_id("username").send_keys("13812345678")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_name("sbtbutton").click()
time.sleep(3)
"""--->2.点击顶部我的订单"""
driver.find_element_by_css_selector(".top-ri-header li a[target]").click()
time.sleep(1)
handle = driver.window_handles
driver.switch_to.window(handle[-1])
"""--->3.在新的窗口中点击地址管理"""
driver.find_element_by_link_text("地址管理").click()
time.sleep(1)
"""--->4.点击新增地址"""
driver.find_element_by_css_selector(".co_blue").click()
"""--->5.在新增地址界面不输入任何信息点击保存收货地址"""
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_id("layui-layer-iframe100001"))
driver.find_element_by_xpath("//button/span").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)
"""--->6.再继续完善地址信息,输入正确的必选项,再次保存收货地址"""
handle = driver.window_handles
driver.switch_to.window(handle[-1])
driver.switch_to.frame(driver.find_element_by_id("layui-layer-iframe100001"))
driver.find_element_by_name("consignee").click()
driver.find_element_by_xpath("//tr[1]/td[2]/input").send_keys("小红")
# driver.find_element_by_name("province").click()
select = Select(driver.find_element_by_id("province"))
select.select_by_value("1")
time.sleep(1)
select1 = Select(driver.find_element_by_id("city"))
select1.select_by_value("2")
time.sleep(1)
select2 = Select(driver.find_element_by_id("district"))
select2.select_by_value("227")
time.sleep(1)
select3 = Select(driver.find_element_by_id("twon"))
select3.select_by_value("240")
time.sleep(1)
driver.find_element_by_id("address").send_keys("东三旗村323号2院310")
driver.find_element_by_name("mobile").send_keys("13812345678")
driver.find_element_by_xpath("//button/span").click()
driver.refresh()
"""--->7.自行设计一条判断代码判断地址新增成功"""
time.sleep(3)
driver.quit()
