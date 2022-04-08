# Data collection and management Day 3

## 동적 크롤링을 사용해 csv 파일로 저장 후 dataframe 만들기
```python
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
from pandas import DataFrame

b = webdriver.Chrome()

url = "http://www.naver.com"
b.get(url)
b.implicitly_wait(10)
search = b.find_element_by_xpath('//*[@id="query"]')
search.send_keys("금융\n")
b.implicitly_wait(10)
b.execute_script("window.scrollTo(0, 300)")
b.find_element_by_xpath('//*[@id="web_1"]/div/div[2]/div[2]/a').click()
b.implicitly_wait(10)
b.switch_to.window(b.window_handles[1])
b.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a/span').click()
b.implicitly_wait(10)
b.execute_script("window.scrollTo(0, 200)")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="tab_section"]/ul/li[2]/a/span').click()
b.implicitly_wait(10)
b.switch_to.frame("frame_ex2")
list1 = []
list2 = []
list3 = []
list_in = []
list_all = []
for i in range(1, 5):
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'/html/body/div/div/a[{i}]').click()
    b.implicitly_wait(10)
    html = b.page_source
    b.implicitly_wait(10)
    s = BeautifulSoup(html, 'html.parser')
    name_data = s.find_all('td', attrs={"class":"tit"})
    b.implicitly_wait(10)
    symbol_data = s.find_all("td", attrs={"class": "symbol"})
    b.implicitly_wait(10)
    number_data = s.find_all("td", attrs={"class":"num"})
    for j in name_data:
        list1.append(j.text)
    b.implicitly_wait(10)
    for j in symbol_data:
        list2.append(j.text)
    for j in number_data:
        j_strip = j.text.strip()
        if j_strip:
            j_strip = j_strip.replace("\n","")
            j_strip = j_strip.replace("\t","")
            j_strip = j_strip.replace(" ","")
        list3.append(j_strip)
    time.sleep(5)
    b.implicitly_wait(10)

for i in range(len(list1)):
    list_in = [list1[i], list2[i], list3[3*i], list3[3*i+1], list3[3*i+2]]
    list_all.append(list_in)

f = open("exc_rate.csv", "w", encoding='utf-8-sig',newline="")
writer = csv.writer(f)
title = ['통화명', '심볼', '현재가', '전일대비', '등락율']
writer.writerow(title)
writer.writerows(list_all)
f.close()

df=pd.read_csv('exc_rate.csv', encoding='utf-8-sig')
df.index=df['통화명']
del df['통화명']

is_pos = []
is_neg = []
for i in range(len(df.등락율)):
    if df.등락율[i][0]=="-":
        is_pos.append(False)
        is_neg.append(True)
    else:
        is_pos.append(True)
        is_neg.append(False)
        
df_p=df[is_pos]
df_n=df[is_neg]
```

