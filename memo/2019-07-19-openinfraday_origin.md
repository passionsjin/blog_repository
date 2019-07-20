- tokten에 대해 알아보기.
- 

## CNCF와 쿠버네티스
 - 쿠버네티스도 자격증이???!!!
 
 
 ## 카카오T택시 사례를 통해 살펴보는 k8s as a services
 
 ### 카카오는 쿠버를 어떻게 쓰나
 - 쿠버 클러스터를 통해 사용
 - 프라이밋 클라우드위에서 작업함.
 ### 장점
 - auto hilling
 - 개발자, 운영자가 편함.
 - 무중단 배포
 - scale out-in (auto 가능)
 
### 카택
- 카나리배포를 이용해 , 배포 이슈를 줄임
-   

## NetApp 
 - container 적용시, storage 이슈가 가장 크다.
 - 컨테이너가 지워지더라도, 데이터는 지속성이 필요함.
 - Data Fabric 데이터의 자유로운 이동
 - Trdent 외장 스토리지 오케스트레이터를 통해 제공.
 - PV PVC
 
 ## knative 기본
 - 장점 : 코드만 있으면 그 외 필요한게 없음
 - 단점 : 테스트가 까다로움. 로컬테스트,,,???
 ### use cases on cloud functions
 - http backend api
 - cronjob
 - cloud event trigger ( vm의crud )
 ### knative
 - kubernetes-based platform to build, deploy, and manage modern serverless workloads
 - serverless function app을 만들수있는건가??
 - CRD
 - 동시접속자보다는 CPU자원에 따른 scaling
 
 ## k8s 에서의 데이터베이스 운영?
 - 