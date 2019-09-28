import bs4 as bs
import urllib.request as req
import time
import xlwt as xl
from xlwt import Workbook
import re
import numpy as np

wb = Workbook()
data_sheet = wb.add_sheet('Data_Sheet')
data_sheet.write(0, 0, 'Title') 
data_sheet.write(0, 1, 'Domain')
href = 'https://old.reddit.com/r/TheOnion/?count=875&after=t3_bp08na'
count = 1
page = 36
while True:
    print('Page: ' + str(page))
    page += 1
    source = req.urlopen(href).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    time.sleep(1)
    titles = soup.find_all('a', attrs = {'data-event-action':'title'})
    for title in titles:
        title_string = title.string
        href = title['href']
        wb.save('TheOnion.xls')
        if href is np.nan:
            domain = href
        else:
            try:
                domain = re.findall(r'(?:www.)?(\w+.(com|org|net|co.uk|in|co|ca|pl|tv|edu|news|us))', str(href), re.DOTALL)[0][0]
            except IndexError:
                domain = 'EW'
        data_sheet.write(count, 0, title_string) 
        data_sheet.write(count, 1, domain)
        count += 1
    next_page = soup.find('a', attrs = {"rel": "nofollow next"})
    href = next_page['href']
    print(href)
