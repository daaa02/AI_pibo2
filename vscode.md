# Setup 
* Visual Studio Code with Keras 초기 설정하기

## 1. Install Anaconda
* https://www.anaconda.com/
* 다운로드 후, 윈도우 키 > Aanaconda Prompt3 실행


        $ conda list
        $ conda update --all -y 
        $ conda --version
        $ python --version

## 2. Install Keras
* Tensorflow & Keras 설치 *(꼭 필요한진 모르겠음)*

        $ pip install tensorflow
        $ pip install keras

* 가상 환경 생성
        
        $ conda create -n keras python=3.9    # conda create -n <이름> <설치할 패키지>

* 가상 환경 실행
  
        $ conda activate keras      # 활성화
        $ conda deactivate keras    # 비활성화

* Keras 패키지 설치
  
        # 둘 중 하나 선택
        $ conda install -c anaconda keras-gpu   # GPU 버전        
        $ conda install -c anaconda keras       # CPU 버전

        # 추가 패키지 설치
        $ conda install -c anaconda pandas -y
        $ conda install -c anaconda xlrd -y
        $ conda install -c anaconda xlwt -y
        $ conda install -c anaconda seaborn -y
        $ conda install -c anaconda scikit-learn -y
        $ conda install pillow -y

## 3. Install VS Code
* https://code.visualstudio.com/
* 다운로드 후, 추가 패키지 설치 ( Ctrl + Shift + x )

        korean language ~                                     # 한국어 설치
        Python, Python for VSCode, Python Extension Pack      # Python 관련 패키지
        CodeRunner
        markdown                                              # 이거 작성한다고

* 글꼴: 설정 > Editor: Font Family > 사용할 폰트를 제일 앞에 추가
* 터미널 열기: Ctrl + `
  * 터미널 열었을 때 (keras) C:\Users\User 바로 되도록 하려면
          
          1-1. 설정 > python path 검색 > Python: Python Path        
          C:\Users\User\anaconda3\envs\keras\python.exe           # Anaconda 가상환경 위치

          1-2. Ctrl + Shift + p > Python: Select Interpreter > "설정하고자 하는 환경"    # 근데 1-1 생략하고 이거만 해도 됨

  * 터미널 열었을 때 conda 어쩌고 에러가 뜬다면

          터미널 창의 우측 상단 '+' 옆의 'v' 클릭 > 기본 프로필 구성 > Command Prompt
     

        
        
