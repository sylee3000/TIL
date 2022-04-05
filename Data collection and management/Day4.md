# Data collection and management Day 4

## selenium 사용
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
id = "dltmddud801"
pw = "tmddud123"
b = webdriver.Chrome()
b.implicitly_wait(10)
b.get("http://www.naver.com")
b.implicitly_wait(10)
lc = b.find_element_by_class_name("link_login")
lc.click()
b.implicitly_wait(10)
#id 입력
in_id = b.find_element_by_id('id')
in_id.click()
pyperclip.copy(id) #복사
in_id.send_keys(Keys.CONTROL,'v') #붙여넣기
b.implicitly_wait(10)
#pw 입력
in_pw = b.find_element_by_id('pw')
in_pw.click()
pyperclip.copy(pw)
in_pw.send_keys(Keys.CONTROL,'v')
b.implicitly_wait(10)
b.find_element_by_id("log.login").click()
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click()
b.implicitly_wait(10)
cur = b.find_element_by_xpath('/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[6]/a/span').click()
b.implicitly_wait(10)
cur = b.find_element_by_xpath('//*[@id="snb"]/ul/li[4]/a').click()
b.implicitly_wait(10)
t = b.find_element_by_xpath('//*[@id="main_content"]/div[2]/ul[1]/li[1]/dl/dt[2]/a').text
t1 = b.find_element_by_xpath('//*[@id="main_content"]/div[2]/ul[1]/li[2]/dl/dt[2]/a').text
print(t, t1)
```