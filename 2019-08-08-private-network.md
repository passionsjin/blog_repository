# 네트워크 구성하기

## VPC
    IP주소 범위와 VPC범위를 설정하고, **Subnet**을 추가하고 **보안 그룹**을 연결한 다음
    **라우팅 테이블**을 구성한다.

## Subnet
### Public subnet
    Internet Gateway, ELB
    Public subnet 내에 있는 NAT를 통하여 Private subnet내에 있는 instances가 인터넷이 가능하게함.
    
### Private subnet
    외부와 차단.
    Private Subnet 내의 인스턴스들은 Private Ip만을 가지고있다.
    다른 서브넷과의 연결만 가능

## 라우팅 테이블
    Ip address에 routing 경로를 정의하여 subnet에서 밖으로 나가는 outbound traffic에 대한 routing 경로를 설정하는 것이다.

## Internet Gateway
    인터넷 라우팅 가능 트래픽에 대한 VPC라우팅 테이블에 대상을 제공하고,
    Public IPv4 주소가 할당된 인스턴스에 대해 NAT를 수행하는 두 가지 목적이 있다.
    

### 참고
* 고가용성 = (사용가능기계시간 - 보수고장수리시간 - 기술개량시간) / 사용가능 기계시간 = 가동률 -> 서비스 중단없이 운영되는 것!?