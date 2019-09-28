import bs4 as bs
import urllib.request as req
import time
import numpy as np
import re
import xlwt 
from xlwt import Workbook  #Workbook is created 
wb = Workbook()  # add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 0, 'Title') 
sheet1.write(0, 1, 'Domain')
count = 1
link = 'https://old.reddit.com/r/nottheonion/'
while 1:
    time.sleep(30)
    source = req.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    titles = soup.find_all('a',attrs={'data-event-action':'title'})
    for title in titles:
        title_string = title.string
        href = title['href']
        if href is np.nan:
            domain = href
        else:
            try:
                domain = re.findall(r'(?:www.)?(\w+.(com|org|net|co.uk|in|co|ca|pl|tv|edu|news|us))', str(href), re.DOTALL)[0][0]
            except IndexError:
                domain = 'EW'
        print(domain)
        sheet1.write(count, 0, title_string) 
        sheet1.write(count, 1, domain)
        wb.save('nottheonion.xls')
        count+=1
    next_page = soup.find('a', attrs = {"rel": "nofollow next"})
    link = next_page['href']
    print(link)
    print(count)
wb.save('nottheonion.xls') 

