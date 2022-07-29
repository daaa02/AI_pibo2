# Git 작업

* 로컬에서 작업한 파일을 github에 업로드
* 복구도 가능하답니다


## 1. git 설치
---
git 설치 확인
```
$ git --version
```
설치가 되어있지 않다면
```
$ sudo apt install git-all
```

## 2. 초기 설정
---
저장소 생성 및 연결

```
$ cd AI_pibo2
$ git init
$ git commit -m "first commit"
$ git branch -M main

$ git remote add origin https://github.com/daaa02/AI_pibo2.git
$ git push -u origin main
```
사용자 정보 설정

```
$ git config --global user.name "깃허브 이름"
$ git config --global user.email "깃허브 메일 주소"
```
언젠가 로그인 하라고 뜬다면
```
username for ~ : 깃허브 닉네임
password for ~ : ***
```

## 3. 업로드🚀
---
* 요약: add -> commit -> push 
* 중간중간 git status로 상태 확인

```
$ git status
```

현재 디렉토리의 모든 파일 업로드 대기열에 추가
```
$ git add . 
```

만약 특정 파일만 업로드 하고 싶다면 
```
$ git add <파일명.py>
```

업로드 대기열에 추가되었는지 확인
```
$ git status

현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 변경 사항:
  (스테이지 해제하려면 "git reset HEAD <파일>..."을 사용하십시오)

	수정함:        Daily/01_weekday.py
	새 파일:       Roleplay/01_magician.py
	새 파일:       Roleplay/Sound/01_magic.wav
```

파일 업로드 하면서 공유할 메세지 내용 입력
```
$ git commit -m "<메모>"    // git commit -m "test"
```

업로드 대기열 깨끗한지 확인
```
$ git status

현재 브랜치 main
브랜치가 'origin/main'보다 1개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
```

**pushhhhhh**
```
$ git push
```

## 4. 끝!
---
github 들어가보면 파일 업로드된 걸 확인할 수 있습니당.
참고로,
* git push: 파일 업로드
* git pull: 파일 다운로드
* git pull --rebase origin main: 깃허브에 업로드 되어 있는 파일과 로컬 파일 동기화
