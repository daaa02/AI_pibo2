

# AI_pibo2

환경 설정만 해도 거의 끄읕 ☆ヾ(*´・∀・)ﾉヾ(・∀・`*)ﾉ☆

**'$' 뒤의 명령어**를 터미널에 한 줄씩 복붙하면 됩니다.

    pi@themaker: ~/AI_pibo2 $ <명령어>  
    // 현재 경로: (/home/pi)/AI_pibo2      

'// ~~' 는 코드나 명령어 설명을 위해 덧붙인 주석이니 참고만 하세용

# 1. 환경 설정

* 개발 환경: Raspberry pi 4, python3.8

## 1-1. wi-fi 연결하기

* 준비물
    * 파이보 뒷면(등) 분리를 위한 드라이버, 
    * Micro HDMI to HDMI 또는 MicroSD카드 리더기(노트북에 내장되어있을 수 있음)

### 1-1-1. 방법 1: HDMI 연결 (또는 putty)

* **putty 접속 중일 때** putty 터미널에서 wi-fi 변경 또는 정보 확인 가능

부팅 후 로그인하기 (ID/PW 입력)

    $ login: pi
    $ password: 1234	// 치고 엔터!

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
	// ip 주소: inet xxx.xxx.xxx.xxx	


### 1-1-2. 방법 2: SD카드 (ㅊㅊ)

전원 꺼진 상태에서 라즈베리파이 보드의 SD카드 제거 후,
PC에 SD카드 삽입 (또는 리더기 연결)

* boot/SSH 빈 파일 만들기
* MicroSD카드/boot/wpa_supplicant.conf 파일 만들기 ([참고](https://www.gloriouscoding.com/da4a2e0d-28f8-4e5c-99ad-277345ef9df7))

		country=GB 
		ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
		network={
		ssid="WIFI_NAME"
		psk="WIFI_PASSWD"       // 비밀번호 없는 경우 psk 입력하지 말고,
		key_mgmt=WPA-PSK        // WPA-SPK 대신 NONE 입력하기
		}

파이보 부팅 후, OLED에서 wi-fi 연결 확인
	
	#NETWORK	
	[W] IP		// xxx.xxx.xxx.xxx
	[S] WIFI_NAME	// kiro_wifi
  

## 1-2-1. 원격 접속 방법 1: Putty	

프로그램 다운로드

* [xming](https://xming.softonic.kr/)
* [putty](https://www.putty.org/)

		1. xming 실행	// 아무 일 안 일어남
		2. putty 실행	 
			1) Category-SSH-X11: [v]Enable X11 forwarding
			2) Category-Session: Host Name에 ip 주소 입력
			3) Saved Session은 선택 사항 (추천)	// save 해두면 1), 2) 과정 생략하고 바로 접속 가능
			4) Open

		3. ID/PW 입력		
			login: pi
			password: 1234	// 치고 엔터!
	
## 1-2-2. 원격 접속 방법 2: VSCode

* vscode.md 파일 참고


## 1-3. 마이크, 스피커 확인하기

녹음 및 재생 장치 연결 확인 

	$ arecord -l
	card: 1 <장치 이름>, device: 0 <장치 이름>	//card, device 숫자 기억!
	
	$ aplay -l		
	card: 1 <장치 이름>, device: 0 <장치 이름>	//card, device 숫자 기억!

장치 사용 설정

: 위 과정에서 확인한 card/device number 와 .asoundrc 파일의 card/device number 같아야 함

*(장치가 연결 되어있지만 안 될 경우 **card number, device number** 수정!)*

	$ nano .asoundrc
	
	pcm.mic {
		...
		pcm "hw:<card number>,<device number>"
	}
	pcm.speaker {
		...
		pcm "hw:<card number>,<device number>"
	}
	
장치 테스트 하고 싶다면

	// 스피커 테스트
	$ speaker-test -t wav
	
	// 녹음
	$ arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
	
	// 재생
	$ aplay --format=S16_LE --rate=16000 out.raw


# 2. 코드 실행

단축 명령어

	$ pibo
	// 놀이 도입 시나리오(src/Intro.py) → 놀이 수행(src/play_scenario/<play_name>.py) →  종료
    
# 3. 기타 (이유정 ㄴㄴ)

## 3-1. 파일 업데이트하기 

	$ cd
	$ ./update.sh

## 3-2. 코드 수정하기

### 3-2-1. 방법 1: 터미널에서 수정하기

수정하고자 하는 파일이 위치한 경로로 접속 (cd 명령어 사용)   
    
        // 현재 위치한 디렉토리를 기준으로 (상대경로)
        ~/AI_pibo2 $ cd src/data
                   $ nano <수정할 파일명>.py
                   
nano 편집기 사용 방법은 검색 필요 (간단)

    
    
  
		 
