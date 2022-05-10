# Setup

## 1. Install Anaconda
* https://www.anaconda.com/
* 다운로드 후, 윈도우 키 > Aanaconda Prompt3 실행


        $ conda list
        $ conda update --all -y 
        $ conda --version
        $ python --version

## 2. Create env
* 가상 환경 생성
  
        $ conda create -n conda python=3.9    # conda create -n <이름> <설치할 패키지>

* 가상 환경 실행
  
        $ conda activate conda      # 활성화
        $ conda deactivate conda    # 비활성화
