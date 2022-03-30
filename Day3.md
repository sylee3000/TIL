# TIL Day 3
## 파일 내용 되돌리기
- git restore (--staged) a.txt : 커밋 진행했을 때
- git rm --cached a.txt : 커밋 진행하지 않았을 때
- vim 화면
    1. i 입력
    2. 편집 진행
    3. 편집 완료 후 esc, :wq 입력
    4. 엔터 입력

## 파일 버전 되돌리기
- git reset
    1. --soft 해시값 : commit 삭제
    2. --mixed 해시값 : staging area + commit 삭제
    3. --hard 해시값 : 전체 삭제
- git reflog 해시값 : 삭제했던 버전 불러오기
- git revert 해시값 : 이전 commit을 취소하는 새로운 commit을 생성

> 커밋 메시지 관련 사이트 : [좋은 git 커밋 메시지를 작성하기 위한 7가지 약속](https://meetup.toast.com/posts/106) [Commit Message Conventions](https://gist.github.com/stephenparish/9941e89d80e2bc58a153)
> 깃허브 페이지 만들기 : [Start Bootstrap](https://startbootstrap.com/)