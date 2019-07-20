* 커뮤니티
 - korea Ceph User Group
 - Open Compute Project
	데이터센터 Open Source HW 생태계 조성
	
Composable and cloud native



* openstack neutron
 - Openstack 네트워킹
 - 가상 네트ㅝ킹 인프라(VNI)에 대한 모든 네트워킹 측면과 Openstack 환경에서 물리 네티워킹 인프라(PNI)의 접근레이어 측면에 관리.
 - 
 
 
* Multi-Cluster Service Mesh
 - 배경:mas복잡성문제해결,MSA트래픽 관리요소를 application코드와 분리
 - multi cluster를 한곳에서 관리가능?
 - 중앙관리의 프록시서버
 - Istio -> (이스티오) Service Mesh Network의 연결,트래픽제어, 텔레메트리 및 보안을 관리할수있는 플랫폼

 - multicloud -> Hybrid Cloud를 연결
 
 - 구현기술 : SNI, split horizon eds, Istio ingress gateway
 
 - 배포시 이슈 : 각 서비스별 설정파일(yaml) 관리가 어려움.  --> Gitops 사용, argo DB툴
 - 
 - ArgoCD : git 과 kubernetes cluster의 yaml 비교 가능
 
 DEMO
 - canary 배포
 
* Traffic mgmt 활용 방안.
 - Istio의 mirroring 기능 활용 소개
	운영서버의 에러슈팅시 에러재현!을 통해 슈팅.
	but 로그재현을 하지않으면? 시간이 단축됨

 - mirroring 기능
	특정 http request의 traffic을 복사하여 지정한 subset에 전달 가능
	product 서버에서 복사된 로그를 통해 stage에서 구현하여 에러재현!! Wow
	
 - Istio telemetry logging
 
 - 정리 : kubernetes 와 Istio의 기능을 통해 멀티클러스터의 운용 및 관리가 가능하다!
 
 
 
 * kubernetes scheduler deep dive
  - scheduler 소개, 확장
  - 새로운 pod이 배포되면 scheduler가 노드를 정해준다??
  - 스케줄러 argorithm
	predicate
  - 
  
  
  
* kafka, flink
 - aws kops
 - eks가 서울리전에 생김?
 - flink는 kubernetes에서 돌아갈수있게 지원하고있음.
 - github/protess/k3a-f3k-k8s
 - app에서 annotation을 통해 dashboard에 정보를 넘길수있다 ( dashboard에서 추가할 필요없음)
 
 
 
* 엔씨소프트의 kubernetes
 - 
 