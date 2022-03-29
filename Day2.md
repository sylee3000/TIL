# TIL Day 2
## .gitignore
- 특정 파일을 버전 관리하지 않겠다고 지정하는 파일
- git add 전에 .gitignore 안에 작성해야 제외 가능
- .gitignore 작성 사이트 : [gitignore.io](https://toptal.com/developers/gitignore) [gitignore 저장소](https://github.com/github/gitignore)

## clone vs. pull
- 원격 저장소의 파일, 폴더들을 로컬 저장소로 가져오는 것
- clone은 다운로드, pull은 업데이트
- git clone URL으로 진행되는 것
    1. 폴더 생성
    2. 내용 복사 (commit)
    3. git init 실행
    4. git remote add origin URL
- pull을 하지 않고 push 진행 시 업데이트 내역이 있으면 오류 발생 가능

## Branch
- 원본을 여러 작업 공간으로 나눠서 독립적으로 작업이 가능
- 원본에 변화를 주지 않고 작업을 할 수 있음
- 생성 : git branch <이름>
- 이동 : git switch <이름> (commit할 파일 있으면 이동 불가능)

## Branch Merge
- merge 종류
    1. Fast-Forward : merge 과정은 없고 브랜치의 포인터만 이동
    2. merge : 서로 다른 두 브랜치를 병합
    3. merge conflict : 서로 다른 두 브랜치가 같은 곳을 수정 시 충돌