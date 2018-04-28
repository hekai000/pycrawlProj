# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0")
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
# cookie = {'name':'foo', 'value': 'bar'}
# driver.add_cookie(cookie)
print driver.get_cookies()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫." not in driver.page_source

driver.close()
