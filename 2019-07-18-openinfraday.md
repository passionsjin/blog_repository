## 해야할것
- service mesh란??
- openstack neutron에 대해 이해하기
- Istio에 대해 정리해보기(모니터링)
- canary 배포란?
- multi cluster를 운영 및 관리하기 위한 기법들?
- argo CD란?
- kubernetes가 어떻게 동작하는지는 알자...
- app에서 로그 dashboard같은곳으로 등록가능함.
- flink란?
- aws kops ???
- eks가 서울리전엔 없었냐??



## Service Mesh란?
    Application의 다양한 부분들이 서로 데이터를 공유하는 방식을 제어하는 방법.
    서비스간 커뮤니케이션을 관리하는 다른 시스템과 달리, App에 구축된 전용 인프라 계층이다.
    따라서 서비스 간 통신을 추상화하여 안전하고,빠르고,신뢰할 수 있게 만든느 전용 InfraStructure Layer이다.
    
    구현은 보통 서비스(MSA 등)의 앞단에 경량화 프록시를 사이드카 패턴으로 배치하여 서비스간 통신을 제어하는 방법으로 구현.
    서비스 간 통신은 사이드카로 배치된 경량화 Proxy를 통해서 동작.
    
    예시로 Istio가 있음.

#### 사이드카?
    클라우드 디자인 패턴의 일종으로,
    기본 Application 외 필요한 추가 기능을 별도의 Apllication으로 구현하고
    이를 동일한 프로세스 또는 컨테이너 내부에 배치하는 것.
    
## Openstack Neutron 이란?
    가상네트워킹 인프라(VNI)에 대한 모든 네트워킹 측면과 Openstack환경에서 물리 네트워킹 인프라(PNI)의 접근 레이어 측면에서 관리.
    
## Istio
####1. Istio란?
    Istio는 마이크로서비스를 서로 연결,관리, 보안기능을 제공하는 오픈 플랫폼(Service Mesh).
    로드밸런싱, 서비스간 인증, 모니터링 등을 어떤 코드의 변경 없이 서비스들 간의 네트워크를 쉽게 만들어준다.
    side-car poxy방식으로 적용되며 Istio control plane의 기능을 사용하여 마이크로서비스들 간의 네트워크 통신을 중계.
####2. Architecture
논리적으로 data plane과 control plane으로 분리됨.
- Data Plane은 마이크로서비스 간의 모든 네트워크 통신을 중계하고 제어하며 일반적인 목적의 정책과 telemetry hub(Mixer)에 따라 동작.
- Control Plane은 프록시가 트래픽을 라우팅 할 수 있도록 관리하고 설정하는 역할을 담당. 또한 Mixer가 정책을 할당하고 telemetry를 수집하도록 함.

## statefull stateless??
###1. stateful
    요청받은 사용자(세션)에 대한 정보를 저장하고 있다.
    
## multitenancy
    하나의 인스턴스에서 여러개의 태넌트 서비스.

## 배포 프로세스
####1. Blue-Green Deployments
     V1가 배포중인 상태일때, V2를 같은 인프라에 배포하고, Test 수행 후 트래픽을 바꿔줌.
###2. A/B testing
    A안 B안을 전체 또는 일부 고객에게 노출하여 검증하는 시스템.
    개선과 동시에 배포할수있네.
 
###3. Canary Releases
    새로운 버전을 Production환경으로 보내 어떻게 동작하는지 모니터링하는 도구로 사용될 수 있다.
    LB를 통해 일부 세션만 물리게 만들어 검증.
   
## Argo CD
GitOps continuous delivery tool for kubernetes.

## flink란
apache storm, spark streaming과 같은 스트리밍 & 배치 프로세싱 플랫폼.

    
## 0 참고문서
* [쿠방의 MSA와 인프라, 배포...](https://medium.com/coupang-tech/%ED%96%89%EB%B3%B5%EC%9D%84-%EC%B0%BE%EA%B8%B0-%EC%9C%84%ED%95%9C-%EC%9A%B0%EB%A6%AC%EC%9D%98-%EC%97%AC%EC%A0%95-a31fc2d5a572)
    