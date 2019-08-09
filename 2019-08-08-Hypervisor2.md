# Hypervisor - 2 ( 사내 강의 )

## Virtual Switch
```buildoutcfg
논리적인 컴퓨터가 접근할 수 있는 논리적인 스위치가 필요.
가상 스위치는 L2 이기때문에 MAC주소로 통신.

 논리적 스위치기 때문에 port가 존재 하지않다.
따라서 기존 네트워크를 적용시키기엔 문제가 많다.
따라서 가상스위치가 아닌 VM NetworkAdapter에 Configuration이 존재
 
```

## SR-IOV ( Single Root I/O Virtualization )
