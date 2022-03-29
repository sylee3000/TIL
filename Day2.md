# TIL Day 2
## .gitignore
- 특정 파일을 버전 관리하지 않겠다고 지정하는 파일
- git add 전에 .gitignore 안에 작성해야 제외 가능
- .gitignore 작성 사이트 : [gitignore.io](https://toptal.com/developers/gitignore) [gitignore 저장소](https://github.com/github/gitignore)

## clone vs pull
- 원격 저장소의 파일, 폴더들을 로컬 저장소로 가져오는 것
- clone은 다운로드, pull은 업데이트
- git clone URL으로 진행되는 것
    1. 폴더 생성
    2. 내용 복사 (commit)
    3. git init 실행
    4. git remote add origin URL
- pull을 하지 않고 push 진행 시 업데이트 내역이 있으면 오류 발생 가능

## 