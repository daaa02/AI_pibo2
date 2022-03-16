

# AI_pibo2

환경 설정만 해도 거의 끄읕


## 1. 환경 설정

### 1-1. wi-fi 연결하기

wi-fi 정보 입력

	$ sudo su
	$ wpa_passphrase WIFI_NAME WIFI_PASSWD >> /etc/wpa_supplicant/wpa_supplicant.conf 

wi-fi 연결 확인

	$ nano /etc/wpa_supplicant/wpa_supplicant.conf
	
	country=GB 
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	network={
        ssid="WIFI_NAME"
        #psk="WIFI_PASSWD"
        psk= xxxxx...
    }
    
wpa_supplicant.conf 파일의 network 부분이 입력한 정보와 같다면 wi-fi 인증 성공 

	$ sudo reboot

시스템 재시작 후, wi-fi 연결 확인 (wlan0)
	
	$ ifconfig	
	* ip 주소: inet xxx.xxx.xxx.xxx	
  

### 1-2. 원격 접속하기	

프로그램 다운로드

* xming: https://xming.softonic.kr/
* putty: https://www.putty.org/

		1. xming 실행
		2. putty 실행	 
			1) Category-SSH-X11: [v]Enable X11 forwarding
			2) Category-Session: Host Name에 ip 주소 입력
			3) Saved Session은 선택 사항
			4) Open

		3. ID/PW 입력		
			login: pi
			password: 1234
	

### 1-3. 마이크, 스피커 확인하기

녹음 및 재생 장치 연결 확인 

	$ cd
	$ arecord -l
	$ aplay -l		 

장치 사용 설정 
(장치가 연결 되어있지만 안 될 경우 수정!)

	$ nano .asoundrc
	
	pcm.mic {
		pcm "hw:<card number>,<device number>"
	}
	pcm.speaker {
		pcm "hw:<card number>,<device number>"
	}
	
장치 테스트 하고 싶다면

	// 스피커 테스트
	$ speaker-test -t wav
	
	// 녹음
	$ arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
	
	// 재생
	$ aplay --format=S16_LE --rate=16000 out.raw


## 2. 코드 실행

디렉토리에서 실행

	$ cd AI_pibo2/src
	$ py Intro.py

또는 단축 명령어

	$ pibo


## 3. 기타

### 3-1. 파일 업데이트하기 

	$ cd
	$ ./update.sh

### 3-2. 코드 수정하기

* 방법 1) 터미널에서 수정하기
			
		$ cd <수정할 파일이 있는 경로>
		ex. 현재 위치가 /AI_pibo2/src 일 경우 $ cd play_scenario

		$ nano <수정할 파일>

* 방법 2) 조금 편하게 수정하기

		 
