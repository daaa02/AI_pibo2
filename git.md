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
$ git config --global user.name "daaa02"
$ git config --global user.email "dyk98498@gmail.com"
```
언젠가 로그인 하라고 뜬다면
```
username for ~ : daaa02
password for ~ :    
```

## 3. 업로드🚀
---
* 요약: add -> commit -> push 
* 중간중간 git status로 상태 확인

```
$ git status
```

현재 디렉토리의 모든 파일 업로드
```
$ git add . 
```

만약 특정 파일만 업로드 하고 싶다면 
```
$ git add <파일명.py>
```

파일 업로드 하면서 공유할 메세지 내용 입력
```
$ git commit -m "<메모>"    // git commit -m "test"
```

**pushhhhhh**
```
$ git push
```


