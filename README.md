# local-k8s-streaming

로컬환경에서 쿠버네티스를 활용한 MicroService Architecture 구현 연습하기 위한 코드로 간단한 각각의 간단한 기능들을 연결하는 코드들이다.


## flask_app : 회원정보 관리 backend

스트리밍 서비스의 로그인, 회원가입, 로그아웃 등 회원정보에 관한 API처리를 하는 backend

/auth/login, /auth/logout, /auth/signup 기능을 사용할 수 있다. 

AWS RDS를 사용하여 관리한다.

Docker build --tag [아이디/image 이름] .   

명령어를 통해 image 를 생성할 수 있으며  

Docker push [아이디/image 이름] 를 통해 docker hub에 업로드가 가능하다. 


## streaming : Video 정보 관리 backend 


스트리밍할 동영상의 url, 이름 등의 정보에 관한 API처리를 하는 backend

/video/list, /video/{vidoeTitle} 명령어 기능을 사용할 수 있다.

mongoDB를 사용하여 관리한다.

Docker build --tag [아이디/image 이름] .   

명령어를 통해 image 를 생성할 수 있으며  

Docker push [아이디/image 이름] 를 통해 docker hub에 업로드가 가능하다. 


## todo-react-app :  frontend

로그인, 비디오 API 요청을 하는 frontend

react build 파일을 nginx에서 사용하는 방식으로 nginx의 reverse proxy를 사용하여 요청에 따라 두가지 backend에 API요청을한다.

[주소]/auth >> flask backend

[주소]/video >> video backend

Docker build --tag [아이디/image 이름] .   

명령어를 통해 image 를 생성할 수 있으며  

Docker push [아이디/image 이름] 를 통해 docker hub에 업로드가 가능하다. 

## deployment , service yaml 파일

k8s 안에서 사용하는 yaml파일로 frontend, backend 1,2 들을 수행하는 pod를 생성하는 deployment yaml 파일과 서비스 디스커버리를 수행하는 service yaml 파일들이다. 

Docker pull [아이디/image 이름] 

해당 명령어를 통해 docker hub에서 pull 기능을 이용해 쿠버네티스의 마스터노드에 image를 받아온 이후 

kubectl create -f [파일이름] 명령어를 통해 deployement , service를 생성할 수 있다. 

 
