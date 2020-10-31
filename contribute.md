# 업무 진행 방식

## master branch

master branch는 배포 가능한 상태를 유지하여 CI/CD 를 통한 배포를 진행합니다.


## 새로운 issue 발생
이슈를 기반으로 브랜치를 생성합니다.

생성한 브랜치는 작업 기준 master 브랜치를 기준으로 생성합니다.

issue가 생겼을 때의 작업 과정은 다음과 같습니다.
 1. issue를 생성하고, 제목에는 간단한 작업에 대한 명시, 내용에는 자세한 사항을 서술합니다.
 2. master에서 pull을 받아 branch를 생성합니다.
 3. 자신의 local branch에서 origin branch로 수시로 push를 합니다.
 4. 피드백을 받아야하거나 작업이 완료되어 merge를 해야할 때는 pull request를 생성합니다.
 5. 동료 피드백이 끝난 후 master로 merge합니다.
 6. CI/CD 자동 배포.
 

## PyCharm Django setting
 ### 가상환경 세팅
  1. sudo python3 -m virtualenv [가상환경을 설치할 경로]
  2. source [경로]/bin/activate 를 하여 가상환경에 접속합니다.
 
 ### 설치
  0. KMU-WINK 슬랙을 통해 settings.py 를 다운로드 받습니다.
  1. settings.py를 프로젝트 내 aws_cloud9_helper_server/settings.py로 저장합니다.
  2. 가상 환경으로 쉘을 실행합니다. (source bin/activate)
  3. pip install -r requirement.txt를 실행합니다.
      

 ### 프로젝트 실행 
 1. 우측 상단의 edit configuration 버튼을 클릭합니다.
 2. 창이 새로 떳다면 좌측 상단의 + 버튼을 누르고 Django server를 클릭합니다.
 3. Host를 0.0.0.0으로 설정합니다.

