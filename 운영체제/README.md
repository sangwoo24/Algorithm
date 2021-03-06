# 운영체제 
----
   사용자와 하드웨어 사이의 중간 매개체로 응용 프로그램의 실행을 제어하고, 자원을 할당 및 관리하며, 입출력제어 및 데이터 관리와 같은 서비스를 제공하는 소프트웨어

- ### 역할
<br><br><br>

## Process [프로세스]
----
- 실행 중인 프로그램, 디스크로부터 메모리에 적재되어 CPU의 할당을 받을 수 있는 프로그램.
- 운영체제로부터 `주소 공간`, `파일`, `메모리` 등을 할당받음. 
  - 프로세스 스택 : 함수의 매개변수, 복귀 주소, 로컬 변수 등의 임시 자료를 저장
  - 데이터 섹션 : 전역 변수들을 저장
  - 힙 : 프로세스 실행 중에 동적으로 할당되는 메모리
<br>


- ### PCB [프로세스 제어 블록]
  - 특정 프로세스에 대한 중요한 정보를 저장하고 있는 운영체제의 자료구조.
  - CPU를 할당받아 작업을 처리하다가도 프로세스 전환이 발생하면 진행하던 작업들을 PCB에 저장한 뒤 CPU를 반환한다. 
  <br>
  - `PCB에 저장되는 정보`
    - 프로세스 식별자 : 프로세스 식별 번호
    - 프로세스 상태 : new, ready, running, waiting, terminated 등의 상태 저장 
    - 프로그램 카운터 : 프로세스가 다음에 실행할 명령어의 주소
    - CPU 레지스터
    - CPU 스케쥴링 정보 : 프로세스의 우선순위, 스케줄 큐에 대한 포인터 등
    - 메모리 관리 정보 : 페이지ㅋ 테이블 또는 세그먼트 테이블 등과 같은 정보를 포함
    - 입출력 상태 정보 : 프로세스에 할당된 입출력 장치들과 열린 파일 목록
<br>


- ### 멀티 프로세스
  - 하나의 응용프로그램을 여러 개의 프로세스로 구성하여 각 프로세스가 하나의 작업(Task)을 처리하도록 하는 것이다.
  - #### 장점
    - 여러 개의 프로세스 중 하나에 문제가 발생해도 다른 프로세스에 영향을 끼치지 않는다.
  - #### 단점
    - Context Switching 과정에서 캐쉬 메모리 초기화 등의 무거운 작업이 진행되어 오버헤드가 발생하게 된다.  
    - 프로세스는 각각 동립된 메모리 영역을 할당받기 때문에 프로세스들 사이의 변수를 공유할 수 없다.

<br><br><br>

## Thread [스레드]
----
- 프로세서의 실행단위로, 한 프로세스 내에서 동작되는 여러가지 독립적인 실행 흐름으로 프로세스 내의 주소 공간이나 자원을 공유할 수 있다.
- `ID`, `프로그램 카운터`, `레지스터 집합`, `스택` 으로 구성된다.
- 같은 프로세스에 속한 다른 스레드와 `코드`, `데이터 섹션` 등의 운영체제 자원들을 공유한다.
- 각각의 스레드는 독립적인 작업을 수행해야 하기 때문에 각자의 `스택`과 `PC` 값을 가지고 있다.
<br>

  - `사용자 레벨 스레드` : 커널 영역의 상위에서 지원되며 사용자 레벨의 라이브러리를 통해 구현된다. `라이브러리` 가 스레드의 생성 및 스케줄링 등을 관리한다. 동일한 메모리 영역에서 스레드가 생성 및 관리되므로 속도가 빠르지만, 여러 개의 사용자 스레드 중 하나의 스레드가 `시스템 호출` 등으로 중단되면 나머지 모든 스레드 역시 중단되는 단점이 있다.
  - `커널 레벨 스레드` : 운영체제가 지원하는 스레드 기능으로 구현되며, `커널` 이 스레드의 생성 및 스케줄링 등을 관리한다. 스레드가 `시스템 호출` 등으로 중단되더라도, 커널은 프로세스 내의 다르스레드를 중단시키지 않고 계속 실행시켜준다. 다만, 사용자 스레드에 비해 생성 및 관리하는 것이 느리다.

<br>

- ### `스택`과 `PC` 를 스레드마다 독립적으로 할당하는 이유
  - `스택`은 함수 호출 시 `전달되는 인자`, `되돌아갈 주소값` 및 `함수 내에서 선언하는 변수` 등을 저장하기 위한 공간.
  - 스레드의 정의에 따라 독립적인 실행 흐름을 추가하기 위한 최소 조건 
  - 독립적인 실행 흐름인 스레드의 명령어 흐름을 기억할 필요가 있기 때문에 `PC 레지스터`를 독립적 으로 할당
<br>

- ### 멀티 스레드
  - 하나의 프로세스를 다수의 실행 단위로 구분하여 자원을 공유하고 자원의 생성과 관리의 중복성을 최소화하여 수행 능력을 향상시키는 것

  - #### 장점
    - 프로세스에 비해서 메모리 공간과 시스템 자원 소모가 줄어들게 됨.
    - 스레드 간의 통신이 필요한 경우 `전역 변수` 의 공간 또는 `Heap` 영역을 이용하여 데이터를 주고받을 수 있다.
    - 스레드의 `Context Switching` 은 프로세스와 달리 `캐시 메모리` 를 비울 필요가 없기 때문에 더 빠르다.
    - 시스템의 처리 능력이 향상되고, 자원 소모가 줄어들며, 응답 시간이 단축되는 장점 때문에 여러 프로세스로 할 수 있는 작업들을 하나의 프로세스에서 스레드를 나눠서 수행하는 것임. 
  - #### 단점
    - 서로 다른 스레드가 데이터와 힙 영역을 공유하기 때문에 어떤 스레드간 메모리 영역에서의 충돌이 발생할 수 있다.
    - 하나의 스레드에 문제가 발생하면 전체 프로세스가 영향을 받는다.
    - 자원 공유의 문제가 발생한다 (동기화 문제)
    - 다른 프로세스에서 스레드를 제어할 수 없다.
- ### 스레드 동기화
  1. 임계 영역(Critical Section) : 공유 리소스에 대해 오직 하나의 스레드 접근만 허용한다.(한 프로세스에 속한 스레드에만 적용)
  2. 뮤텍스(Mutex) : 공유 리소스에 대해 오직 하나의 스레드 접근만 허용한다. (다른 프로세스에 속한 스레드에게도 적용)
  3. 이벤트(Event) : 특정 사건 발생을 다른 스레드에게 알림
  4. 세마포(Semaphore) : 한정된 개수의 자원을 여러 스레드가 사용하려고 할 때, 접근을 제한
<br><br><br>

## 멀티 프로세스 vs 멀티 스레드
---
  - `멀티 스레드` 는 `멀티 프로세스` 보다 적은 메모리 공간을 차지하고 Context Switching이 빠르다는 장점이 있지만, 오류로 인해 하나의 스레드가 종료되면 전체 스레드가 종료될 수 있다는 점과 동기화 문제를 안고 있다.
  - `멀티 프로세스` 방식은 하나의 프로세스가 죽더라도 다른 프로세스에는 영향을 끼치지 않고 정상적으로 수행된다는 장점이 있지만, `멀티 스레드` 보다 많은 메모리 공간과 CPU 시간을 차지한다는 단점이 존재한다.
<br><br><br>


# 스케줄러
----
- 프로세스를 스케줄링하기 위한 Queue에는 세 가지 종류가 존재한다.
  - Job Queue : 현재 시스템 내에 있는 모든 프로세스의 집합
  - Ready Queue : 현재 메모리 내에 있으면서 CPU 를 잡아서 실행되기를 기다리는 프로세스의 집합
  - Device Queue : Device I/O 작업을 대기하고 있는 프로세스의 집합


### 장기스케줄러
- 디스크에서 메모리로 작업을 가져와 처리할 순서를 결정한다.
- 프로세스에 메모리(및 각종 리소스)를 할당한다.
- 프로세스의 상태
  - new -> ready(in memory)
### 중기스케줄러
- CPU를 사용할 권한을 부여 할 프로세스를 결정한다.
- swap 기능의 일부로 메모리에 부분적으로 프로세스를 적재하고, 일시중지된 프로세서의 원인을 해결하면 다시 준비 상태로 만드는 스케줄러.
- 프로세스의 상태
  - stop -> ready
### 단기스케줄러
- 메모리에 적재된 프로세스 중 CPU를 할당하여 실행 상태가 되도록 결정한다.
- 프로세스에 직접 CPU를 할당한다.
- 프로세스 상태
  - ready -> running -> waiting -> ready
<br><br><br>

# CPU 스케줄러
---
- `준비 큐(Ready Queue)`에 있는 프로세스들을 스케줄링한다.
<br>

- `선점` 스케줄링 : 현재 실행 중인 프로세스를 인터럽트할 수 있거나 준비 상태로 이동할 수 있는 경우의 스케줄링
  -  프로세스가 장시간 동안 프로세서를 독점하는 것을 방지
  -  실시간, 대화식 시분할 시스템에 사용
  -  오버헤드가 커질 수 있다
<br>

- `비선점` 스케줄링 : 한 프로세스가 자원을 선택했을 때, 다른 프로세스가 해당 자원을 뺏을 수 없는 경우의 스케줄링
  - 모든 프로세서를 공정하게 관리
  - 대기 중인 프로세스는 영향을 받지 않으므로 응답시간을 예측하기 쉬움
  - 하나의 프로세스가 장시간 CPU를 독점할 수 있다.
<br>

### FCFS(First Come First Served)
  - #### 특징
    - 먼저 온 순서대로 처리.
    - 비선점 스케줄링

  - #### 문제점
    - 소요시간이 긴 프로세스가 먼저 도달하면 효율성이 낮아진다.
<br>

### SJF(Shortest Job First)
  - #### 특징
    - 다른 프로세스가 먼저 도착했어도 실행 시간이 가장 짧은 프로세스에게 할당하는 스케줄링
    - 비선점 스케줄링
    - 평균 대기 시간이 짧다.

  - #### 문제점
    - 초기의 긴 작업이 뒤로 밀려나 `기아상태` 가 발생할 수 있다.
    - 운영체제가 프로세스의 종료 시간을 예측하기 어렵다.
<br>

### SRT(Shortest Remaining time First)
  - #### 특징
    - 새로운 프로세스가 도착할 때 마다 새로운 스케줄링이 이루어진다.
    - 선점 스케줄링
    - 현재 수행중인 프로세서의 남은 실행시간 보다 더 짧은 실행시간을 가지는 새로운 프로세스가 도착하면 CPU를 뻇긴다.

  - #### 문제점
    - 소요시간이 긴 프로세스가 먼저 도달하면 효율성이 낮아진다.
    - 새로운 프로세스가 도착할 때 마다 스케줄링을 다시하기 때문에 운영체제가 프로세스의 종료 시간을 예측하기 어렵다.
<br>

### SRT(Shortest Remaining time First)
  - #### 특징
    - 새로운 프로세스가 도착할 때 마다 새로운 스케줄링이 이루어진다.
    - 선점 스케줄링
    - 현재 수행중인 프로세서의 남은 실행시간 보다 더 짧은 실행시간을 가지는 새로운 프로세스가 도착하면 CPU를 뻇긴다.

  - #### 문제점
    - 남은 시간이 더 적은 프로세스와 Switching을 해야하므로 추가적인 작업이 필요하다.
    - 새로운 프로세스가 도착할 때 마다 스케줄링을 다시하기 때문에 운영체제가 프로세스의 종료 시간을 예측하기 어렵다.
<br>

### 우선순위 스케줄링(Priority Scheduling)
  - #### 특징
    - 우선순위가 가장 높은 프로세스에 CPU를 할당하는 스케줄링.
    - 우선순위가 동일한 프로세스들은 `FCFS` 로 스케줄링 한다.
    - 선점형 스케줄링 방식
      - 더 높은 우선순위의 프로세스가 도착하면 실행중인 프로세스를 멈추고 CPU를 선점한다.
    - 비선점형 스케줄링 방식
      - 더 높은 우선수위의 프로세스가 도착하면 Ready Queue의 Head에 넣는다.

  - #### 문제점
    - 우선순위가 낮은 프로세스는 무한정 기다려야 한다.

  - #### 해결책
    - 오래 기다리면 우선순위를 높혀준다. (= 에이징)
<br>

### RR(Round Robin)
- 시분할 시스템을 위해 설계한 스케줄링
- 순서대로 돌아가면서(선착순으로) 실행하되, 규정 시간을 정한다. (시분할과 유사)
  - #### 특징 
    - 각 프로세스는 동일한 크기의 `할당 시간` 을 갖게 된다.
    - `할당 시간` 이 지나면 프로세스는 선점당하고 Ready Queue의 제일 뒤에 가서 다시 줄을 선다.
    - CPU 사용시간이 랜덤한 프로세스들이 섞여있을 경우에 효율적이다.
    - `응답 시간` 이 빨라진다.
      - 어떤 프로세스도 일정 시간 이상 기다리지 않는다.
  - #### 문제점
    - 설정한 `규정 시간량(time quantum)` 이 너무 커지면 `FCFS` 와 같아진다.
    - 설정한 `규정 시간량(time quantum)` 이 너무 작아지면 Switching으로 인한 오버헤드가 발생한다.
<br>

### HRN 스케줄링(Highest Response Rate Next)
- `SJF` 스케줄링의 긴 작업과 짧은 작업간의 불평등을 보완한 스케줄링 방식.

  -   #### 특징
      -   SJF 스케줄링에서 발생할 수 있는 `아사현상` 을 해결하기 위해 만들어짐
      -   서비스를 받기 위해 기다린 시간과 CPU 사용 시간을 고려하여 스케줄링.
          -   우선순위 = (대기 시간 + CPU 사용 시간) / CPU 사용 시간
<br>

### 동기 vs 비동기
- 동기 : 어떠한 일들을 순차적으로 진행
- 비동기 : 병렬구조로 여러 일을 동시에 진행하지만 어느 일이 먼저끝나는지 알 수 없다.

<br><br>

## 프로세스 동기화
- ### Critical Section
  - 동일한 자원을 동시에 접근하는 작업을 실행하는 코드 영역을 Critical Section 이라 칭한다.

- ### Critical Section Problem
  - 프로세스들이 Critical Section 을 함께 사용할 수 있는 프로토콜을 설계하는 것
  
  - #### Lock
    - 하드웨어 기반 해결책으로, 동시에 공유 자원에 접근하는 것을 막기 위해 Critical Section 에 진입하는 프로세스는 Lock을 획득하고, Critical Section을 빠져나올 때, Lock을 방출함으로써 동시에 접근이 되지 않게 한다.
  - #### Semaphores
    - 소프트웨어상에서 Critical Section 문제를 해결하기 위한 동기화 도구
      - 카운팅 세마포 : 가용한 개수를 가진 자원에 대한 접근 제어용으로 사용한다.
      - 이진 세마포(Mutex) : 0 과 1 사이의 값만 가능하며, 다중 프로세스들 사이의 Critical Section 문제를 해결하기 위해 사용한다.

## 🔥 용어
- 교착상태(Dead Lock) : 상호 배제에 의해 나타나는 문제점으로, 둘 이상의 프로세스들이 자원을 점유한 상태에서 서로 다른 프로세스가 점유하고 있는 자원을 요구하며 무한정 기다리는 현상을 의미.
- 레이스컨디션 : 한정된 자원을 동시에 이용하려는 여러 프로세스가 자원의 이용을 위해 경쟁을 벌이는 현상.
- IPC(Inter Process Communication) : 프로세스 간 통신 
  - 멀티 프로세싱 : 다수의 CPU 가 서로 협력적으로 일을 처리하는 것을 의미한다(= 멀티코어, 쿼드코어)
  - 멀티 프로그래밍 : 입출력 작업의 종료를 대기할 동안 하나의 프로세서에서 다른 프로그램을 수행할 수 있도록 하는 것
