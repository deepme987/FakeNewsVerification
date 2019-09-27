# import pandas as pd
from selenium import webdriver
import time

# driver = webdriver.Chrome('C:\\Users\\preet\\AppData\\Local\\Programs\\
# Python\\Python37-32\\ScrapingEnv\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Firefox('C:\\Users\\preet\\AppData\\Local\\Programs\\
# Python\\Python37-32\\ScrapingEnv\\chromedriver_win32\\geckodriver.exe')

geckodriver = 'C:\\Users\\deepm\\Downloads\\geckodriver.exe'
 
options = webdriver.options()
options.add_argument('-headless')
 
browser = webdriver.Firefox(executable_path=geckodriver, options=options)

print("Hello")
#    browser.get('https://app.neilpatel.com/en/traffic_analyzer/overview?lang=en&locId=2840&domain='+domain)
browser.get('https://app.neilpatel.com/en/traffic_analyzer/overview?domain=yahoo.com&locId=2840&lang=en')
time.sleep(60)
#    results = browser.find_elements_by_tag_name('div')
results = browser.find_elements_by_xpath("//*[contains(@class = 'css-1ex6ef5')]")
# results1 = browser.find_elements_by_xpath("//*[contains(@class = 'css-sifqy9')]")
#    for result in results:

#        print(result.get_attribute('class'))
print(len(results))
# for result in results1:
#     print(result.get_attribute('class'))
#     print(len(result))
print('success')
# print(domain_set)

