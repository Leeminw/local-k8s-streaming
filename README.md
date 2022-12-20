# local-k8s-streaming

로컬환경에서 쿠버네티스를 활용한 MicroService Architecture 구현 연습하기 위한 코드로 간단한 각각의 간단한 기능들을 연결하는 코드들이다.


## flask_app : 회원정보 관리 backend

## streaming : Video 정보 관리 backend 

## todo-react-app :  frontend


쿠버네티스 상에서 사용하기 위한 도커파일들이 각각의 폴더에 내장되어있어 각각의 폴더를 build한 후 

docker build 명령어를 통해 docker image 를 제작한 후 docker hub에 push/pull 기능을 이용해 쿠버네티스의 마스터노드에서 받아와 사용한다.
