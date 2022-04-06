# Data collection and management Day 4

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