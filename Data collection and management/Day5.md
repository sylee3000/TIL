# Data collection and management Day 5

## 정적 크롤링

```python
#정적 크롤링
import csv#csv파일을 저장하기 위한 외부모듈
import requests#외부모듈 불러오기(정적 크롤링)
from bs4 import BeautifulSoup#(쉽게 data 접근을 위한 도구)
#정적 크롤링
url='https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%95%94%ED%98%B8%ED%99%94%ED%8F%90'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
r=requests.get(url,headers=headers)#서버에 웹페이지 요청
#data접근
#print(r.text)#<html>...</html>
soup=BeautifulSoup(r.text,'html.parser')#정렬도구(단수)
#1.연관그룹을 이용한 data접근
l_all=[]
#data=soup.find_all('div',attrs={"class":"news_area"})
data=soup.select('div.news_area')#특정 data의 영역을 선택 (복수)
#data1=soup.select('li')
for i in data:
    l_all.append([i.select_one('a.news_tit').text,i.select_one('div.news_dsc').text])
    #print(i.find("div",attrs={"class":"news_dsc"}).text)#특정한 영역의 data 를 선택(단수)
#2. 단일 이름을 이용한 접근

l1=[]
l2=[]
data1=soup.select('a.news_tit')
data2=soup.select('div.news_dsc')
for i in data1:
    l1.append(i.text)
for i in data2:
    l2.append(i.text)
l_all=list(zip(l1,l2))

#저장
with open("save_data.csv","w",encoding="utf-8-sig",newline='') as f:
    w=csv.writer(f)
    w.writerow(['제목','내용'])#한번(한줄)입력(1차원 data)
    w.writerows(l_all)#복수(여러줄)입력(2차원 data)반복은 2차원의 원소의 갯수로 결정
#로드(저장된 data 출력)
with open("save_data.csv","r",encoding="utf-8-sig",newline='') as f:
    r=csv.reader(f)#모든정보 불러오기(모든 줄 불러오기)(2차원)
    for i in r:#정보를 개별 추출(한줄 불러오기)(2차원->1차원)
        print(i)#개별 단어 내용 출력(1차원)
        print(i[0],i[1])#개별원소 출력(1원소)

```

## 동적 크롤링
```python
#동적 크롤링
import time
#import selenium #웹 자동화
from selenium import webdriver#웹 페이지 컨트롤러
from bs4 import BeautifulSoup
#op=webdriver.ChromeOptions()#웹 컨트롤러의 옵션틀 설정
#op.add_argument("window-size=1920x1080")#지정되 크기로 페이지 오픈
#봇으로 인식되지 않도록 설정을 한다.(단,직접적으로 페이지를 연다면 사용하지 않아도 된다.)
#op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
#b=webdriver.Chrome(options=op)#상위에 지정한 옵션으로 크롬 실행
#1.웹 자동화 장치 구축
b=webdriver.Chrome()
b.maximize_window()
#2.웹 자동화 장치실행(원하는 페이지까지 이동)
url="http://google.com"
b.get(url)
b.implicitly_wait(10)#활성화대기(웹 창 전부가 완성되었을때 동작 그리고 완성이 진행되지 않으면 예외 발생)
in_data=b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')#특정한 장소를 선택
in_data.send_keys("구글무비\n")#값입력
b.implicitly_wait(10)#활성화대기
link=b.find_element_by_xpath('//*[@id="tads"]/div/div/div/div/div[1]/a/div[1]/span')#링크 선택
link.click()#클릭 동작
b.implicitly_wait(10)#활성화대기
while True:#모든 내용 로드를 위한 동작
    info_n = b.execute_script("return document.body.scrollHeight")#로드된 내용의 최하단 크기확인
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")#로드된 내용의 최하단으로 이동
    # 확장
    time.sleep(2)
    next_n = b.execute_script("return document.body.scrollHeight")
    if info_n == next_n:  # 모든 내용을 담고있는 페이지 최하단
        break
html=b.page_source#3.페이지 크롤링
s=BeautifulSoup(html,'html.parser')#정렬도구(단수)
data=s.select('div.Epkrse')
for i in data:
    print(i.text)

import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    ,"Accept-Language":"ko-KR,ko"}
r=requests.get('https://play.google.com/store/movies',headers=headers)
s=BeautifulSoup(r.text,'html.parser')
data=s.select('div.Epkrse')
for i in data:
    print(i.text)

```