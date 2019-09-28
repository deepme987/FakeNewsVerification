'''
Exctracting Domain Score from Ubersuggest

1. Read disctinct sites from TheOnion.xls
2. Search the site score on Ubersuggest using Selenium
3. Extract the text of the tag that contains the Domainscore

'''

import pandas as pd
from selenium import webdriver
import time

data = pd.read_excel("TheOnion.xls", sheet_name = 'Sheet2')
domain_set = set(data['Domain'])
##driver = webdriver.Chrome('C:\\Users\\preet\\AppData\\Local\\Programs\\Python\\Python37-32\\ScrapingEnv\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Firefox('C:\\Users\\preet\\AppData\\Local\\Programs\\Python\\Python37-32\\ScrapingEnv\\chromedriver_win32\\geckodriver.exe')

geckodriver = 'C:\\Users\\preet\\Downloads\\geckodriver.exe'
 
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
 
browser = webdriver.Firefox(executable_path=geckodriver, options=options)
 


print("Hello")
for domain in domain_set:
    browser.get('https://app.neilpatel.com/en/traffic_analyzer/overview?lang=en&locId=2840&domain=facebook.com')

    time.sleep(90)

    results = browser.find_elements_by_xpath("//div[@class='css-1defk8e']//div[@class='css-1ex6ef5']")
    ##results1 = browser.find_elements_by_xpath(".//div[contains(@class, 'css-sifqy9')]")
    ##for result in results:
    ##    print(result.text)
    print(results)
    ##    print(len(result))
print('success')

