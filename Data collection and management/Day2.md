# Data collection and management Day 2

## 정규식
- 원하는 형태에 따른 문자열 선택
1. match("문자열") : 처음부터 일치
2. search("문자열") : 일치하는 문자 있는지 확인
3. findall("문자열") : 일치하는 모든 문자의 리스트 출력
> . : 문자 / ^ 시작 / $ 끝

## BeautifulSoup 사용
```python
import requests
from bs4 import BeautifulSoup
url = '크롤링 할 url'
r = requests.get(url) # html 값 가져옴
soup = BeautifulSoup(r.text, "html.parser")
#data = soup.select("") 
#data = soup.find_all("", attrs={"":""})
```