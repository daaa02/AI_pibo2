# AI_pibo2




# 1. 환경 설정

## 1-1. wi-fi 연결

### 1-1-1. wi-fi 정보 입력

	$ sudo su
	$ wpa_passphrase WIFI_NAME WIFI_PASSWD >> /etc/wpa_supplicant/wpa_supplicant.conf 

### 1-1-2. wi-fi 연결 확인
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
  

## 1-2. 원격 접속 하기	

### 1-2-1. 프로그램 다운로드

xming: <https://xming.softonic.kr/>
putty: <https://www.putty.org/>

### 1-2-2. 원격 접속

1. xming 실행
2. putty 실행
		 
		1) Category-SSH-X11: [v]Enable X11 forwarding
		2) Category-Session: Host Name에 ip 주소 입력
		3) Saved Session은 선택 사항
		4) Open
3. ID/PW 입력
		
		login: pi
		password: 1234
				 
 
