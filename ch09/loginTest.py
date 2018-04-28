# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Firefox()

driver.get("file://H:\kdcsTestProj\crawlpyProj\ch09\9.4.4.login.html")
username = driver.find_element_by_name('username')
password = driver.find_element_by_xpath(".//*[@id='loginForm']/input[2]")
login_button = driver.find_element_by_xpath("//input[@type='submit']")
select = Select(driver.find_element_by_xpath('//form/select'))
select.select_by_value("name")
username.send_keys("qiye")
password.send_keys("qiye_pass")
time.sleep(5)
login_button.click()
select.deselect_all()
time.sleep(5)
