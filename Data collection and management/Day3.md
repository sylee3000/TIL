# Data collection and management Day 3

## sqlite3
```python
f = sqlite3.connect("file_name.db") # file_name.db파일 연결

## 저장
c = f.cursor() # 시작 지점 지정
# c.execute() : 한줄 작성
c.execute("DROP TABLE IF EXISTS table_name") # table_name 테이블 초기화
c.execute("CREATE TABLE table_name(data1 text, data2 text, data3 text)") # table_name 테이블 생성 / 3개의 데이터
c.execute("INSERT INTO table_name VALUES(:data1, :data2, :data3)", {"data1":a, "data2":b, "data3":c}) 
# c.executemany() : 여러 줄 작성 (제공된 data(list)의 길이로 반복 횟수 결정)
c.executemany("INSERT INTO table_name VALUES(:data1, :data2, :data3)", [{"data1":a, "data2":b, "data3":c}, {"data1":a, "data2":b, "data3":c}, {"data1":a, "data2":b, "data3":c}]) 
f.commit() # 저장 마무리
f.close()

## 출력
f = sqlite3.connect("file_name.db)
c = f.cursor()
c.execute('SELECT * FROM table_name")
for i in c.fetchall(): # fetchall : db에 저장되어있는 내용 출력
    print(f"data1 : {i[0]}, data2 : {i[1]}, data3 : {i[2]}")
```