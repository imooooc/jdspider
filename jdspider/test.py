from selenium import webdriverimport  timebrowser = webdriver.Chrome()browser.get('https://www.baidu.com')html = browser.page_sourcetime.sleep(5)input = browser.find_element_by_id('kw')input.send_keys('小拾')button = browser.find_element_by_id('su')button.click()time.sleep(3)browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')time.sleep(5)browser.close()## from selenium import webdriver# import time# #打开百度# driver=webdriver.Chrome()# driver.get("https://www.baidu.com/")# #搜索selenium，制造含有滚动条的环境# kw=driver.find_element_by_id("kw")# kw.send_keys("selenium")# su=driver.find_element_by_id("su")# su.click()# for i in range(1, 10000, 10):#     js = "document.documentElement.scrollTop={value}".format(value=i)#     driver.execute_script(js)