# QUEUE
<br>



<br><br>

##  특징 
- 선형 자료구조의 일종으로 먼저 넣은 데이터가 먼저 나오는 FIFO(First In First Out) 구조입니다.
- 큐에 새로운 Data가 들어오면 enqueue를, Data가 삭제될 때는 dequeue를 수행합니다.
- 주로 컴퓨터 버퍼에 사용되며 입력이 초과되어 작업을 진행하지 못할 시, 버퍼(큐)를 만들어서 대기시킨 후 추후에 순차적으로 작업을 진행시킵니다.
- 데이터를 추가한 순서대로 제어할 수 있기 때문에 스트리밍(Streaming), 너비 우선 탐색(BFS), 프로세스 스케줄링 등 에서 사용됩니다.

<br>

## 1. 선형 큐

<center>
<img width="412" alt="스크린샷 2020-10-07 오후 5 32 35" src="https://user-images.githubusercontent.com/56511253/95307034-1cd07300-08c3-11eb-9887-c93dd7cba5c0.png">
</center>

- 1부터 5까지 차례대로 들어온 것이며 `dequeue`연산을 하게 되면 1이 출력됩니다.
<br>

<center>

![스크린샷 2020-10-07 오후 5 28 57](https://user-images.githubusercontent.com/56511253/95306667-a9c6fc80-08c2-11eb-8e91-bd34fafd148e.png)
</center>


- `선형 큐`에서 삽입 및 삭제를 반복하다 보면, `rear`가 맨 마지막 인덱스를 가리키고, 나머지 앞부분은 비어 있을 수 있지만 이를 꽉찼다고 인식해버립니다 --> `메모리 낭비`
   - 이는 실제 데이터는 삭제 때마다 한 칸 앞으로 이동시키지 않았고, 인덱스 단위로 큐의 연산을 진행했기 때문입니다.
- 또한 `선형 큐`는 큐에 Data가 꽉 찼다면 더 추가할 수 없습니다.
- 이러한 문제점들을 해결하기 위해 `원형 큐`를 사용합니다.
<br><br>

### 1-1. 선형 큐 시간복잡도
- 삭제 연산 복잡도 : O(1)
    <br>
- 삽입 연산 복잡도 : O(N)
  - front가 배열에 끝에 도달하고, 배열의 앞부분이 공백상태가 되어 있더라도 삽입하지 못하기 때문에 원소들을 왼쪽으로 이동시켜야 하므로 O(N)의 시간이 소요된다.

<details>
<summary><font size = "5em" color = "red">선형 큐 구현</font></summary>
<div markdown = "1"><br>

<details>
<summary>list로 구현</summary>
<div markdown = "1"> 

- 파이썬에서 큐를 사용하는 가장 간단한 방법.
- list객체의 `pop(0)` 함수를 호출하면 첫 번째 데이터를 제거할 수 있음.
- `list.insert(0,value)` 를 통해 맨 앞에서 데이터를 삽입 가능.
- `pop(0)`과 `insert(0,value)`는 `O(N)`의 복잡도를 가지고 있기 때문에 성능이 좋지 않음.
  - 첫번째 데이터를 제거하면 모든 데이터를 앞으로 한칸씩 당겨와야 하기 때문.
- 따라서 보통 `collection` 모듈의 `deque`를 사용.
<br>

```python
queue = [1,2,3]

# push
queue.append(4)
queue.append(5)

print(queue)
>>[1,2,3,4,5]

# pop
queue.pop(0)
queue.pop(0)

print(queue)
>>[1,2,3]
``` 
<br><br></div></details>

<details>
<summary>deque로 구현</summary>
<div markdown = "1"> 

- deque의 `popleft()`와 `appendleft(value)` 는 모두 O(1)의 시간복잡도를 가지고 있음 -> list 대비 성능 향상.
- 하지만 내부적으로 `LinkedList` 를 사용하고 있기 때문에 i 번째 데이터에 접근하기 위해서는 `O(N)`의 복잡도가 발생.
```python
from collection import deque

deque = deque([1,2,3])
deque.append(4)
deque.appendleft(0)

print(deque)
>> deque([0, 1, 2, 3, 4])
 
deque.pop()
deque.popleft()

print(deque)
>> deque([1, 2, 3])
```
<br><br></div></details>

<details>
<summary>queue모듈로 구현</summary>
<div markdown = "1"> 

- `queue`모듈의 `Queue` Class 사용.
- 주로 멀티 쓰레드 환경에서 사용되며, 내부적으로 `Locking`을 지원하여 여러개의 쓰레드가 동시에 데이터를 추가하거나 삭제할 수 있음.
- `deque`와 다르게 방향성이 없음. 따라서 추가와 삭제가 하나의 메서드로 처리됨.
- 데이터를 추가하기 위해서는 `put(value)`, 삭제하기 위해서는 `get()`을 사용함.
- Data 추가 삭제는 `O(1)`, 데이터 접근은 `O(N)`의 복잡도를 가짐.


```python
from queue import Queue

que = Queue()
que.put(1)
que.put(2)
que.put(3)

print(que.get())
>> 1
print(que.get())
>> 2
print(que.get())
>> 3

```
- queue 모듈에서 제공하는 LifoQueue, PriorityQueue

```python
import queue
l_queue = queue.LifoQueue()
p_queue = queue.PriorityQueue()
```
<br><br></div></details>

<details>
<summary>Class로 구현</summary>
<div markdown = "1"> 

```python
class MyQueue:
    def __init__(self):
        self.queue = []
    
    def push(self,value):
        self.queue.append(value)
    
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[-1]

    def printQueue(self):
        print(self.queue)



if __name__ == "__main__":
    myqueue = MyQueue()
```
</div></details>
</div></details>
<br><br><br><br>


## 2. 원형큐
<center><img width="408" alt="스크린샷 2020-10-07 오후 5 43 40" src="https://user-images.githubusercontent.com/56511253/95308266-a59bde80-08c4-11eb-89f5-6134d1ff3b32.png"></center>

- 선형 큐와 동일하게 1차원 배열을 이용하지만 처음과 끝이 원형처럼 이어져 있다고 가정합니다.
- 큐를 원형으로 생각해야하기 때문에 mod연산을 사용해야합니다.
- 선형 큐에서는 필요했던, 삭제 시 데이터들을 한번씩 앞당겨주는 불필요한 작업들을 없앨 수 있다.

<details>
<summary><font size = "5em" color = "red">원형 큐 구현</font></summary>
<div markdown = "1"> 
<br><br>

1. Full 상태와 Empty상태를 구별하기 위해 원형 큐에서는 1개의 배열 공간이 낭비됨.
2. enqueue를 할 시, rear은 (rear + 1) % max를 통해 마지막 index에서 data가 추가가 되더라도 다시 0번째 index로 넘어옴. (dequeue도 동일)
    - isEmpty : rear와 front의 index가 동일할 시 빈 배열이라고 판별.
    - isFull  : rear에서 앞으로 index를 옮겼을 때, front와 동일한 index일 경우 1개의 남긴 배열공간을 침범하기 때문에 Full이라고 판별한다.
```python
class circularQueue:
    def __init__(self,max_size):
        self.rear = 0
        self.front = 0
        self.max = max_size
        self.que = [None for i in range(self.max)]

    def isEmpty(self):
        return True if self.rear == self.front else False
        
    def isFull(self):
        return True if (self.rear + 1) % self.max == self.front else False

    def enqueue(self,data):
        if self.isFull():
            print("is Full!! ")
        else:
            self.rear = (self.rear + 1) % self.max
            self.que[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("is Empty!!")
        else:
            self.front = (self.front + 1) % self.max
            return self.que[self.front]   

    def printQueue(self):
        front = self.front
        rear = (self.rear + 1) % self.max

        while (front + 1) % self.max != rear: 
            front = (front + 1) % self.max
            print(self.que[front],end='')
        print(" ")
if __name__ == "__main__":
    queue = circularQueue(5)
    for i in range(4):
        queue.enqueue(i)
        queue.printQueue()

    for i in range(4):
        queue.dequeue()
        queue.printQueue()
```
</div></details><br><br><br><br>

## 3. Linked 큐

![스크린샷 2020-10-07 오후 10 09 08](https://user-images.githubusercontent.com/56511253/95334957-ba3e9d80-08e9-11eb-9102-0186a88df88f.png)

- 배열과 다르게 추가, 삭제시 유연성이 생기기 때문에 배열보다 공간을 효율적으로 이용 가능하다.
  - 크기가 정해진 배열과 다르게 Linked List는 최대 원소개수의 제약이 없기 때문에 공간적 효율성이 증대된다.
  - 배열에선 원소를 dequeue하게되면 원소들을 하나씩 밀어넣어줘야 하지만, Linked List는 삽입과 삭제가 바로 이루어짐.  
- 크기에 제한이 없지만 속도가 느리다.

<details>
<summary><font size = "5em" color = "red">Linked Queue 구현</font></summary>
<div markdown = "1"> 
<br>

- 설계 과정
<br>

<img src = "https://user-images.githubusercontent.com/56511253/95335883-e1e23580-08ea-11eb-9bfe-5c4704353082.png" width = "30%" height = "30%">
<br><br>


- Linked List와 동일하게 Node를 구성.
- enqueue : rear가 가리키는 곳에 Data를 저장.
- dequeue : front가 가리키는 곳에있는 Data를 return 후, front는 다음에 있는 Node로 이동.
```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedQueue:
    def __init__(self):
        self.front = ''
        self.rear = ''
        self.qCount = 0

    def isEmpty(self):
        return True if self.front == '' else False  
    
    def qSize(self):
        return self.qCount

    def enqueue(self,data):
        node = Node(data)

        if self.front == '':
            self.front, self.rear = node, node
             
        else:
            self.rear.next = node
            self.rear = node
        self.qCount += 1

    def dequeue(self):
        front = self.front
        
        if front == '':
            print("Delete Error(Empty)!!")
            return 

        if self.front == self.rear:
            self.rear, self.front = '', ''
        else:
            self.front = self.front.next
            del front

        self.qCount -=1 

    def printQueue(self):
        front = self.front

        if front == '':
            print("Queue is Empty!!")
            return 
        
        print("Linked Queue : [",end = ' ')
        while front:
            print(front.data,end=' <- ')
            front = front.next
        print("x]")


if __name__ == "__main__":
    que = linkedQueue()

    while True:
        print("==========Linked Queue Test!!============")
        print("1. enqueue")
        print("2. dequeue")
        print("3. Queue size?")
        print("4. imEmpty?")
        print("5. printQueue")
        print("6. exit")

        n = int(input())

        if n == 1:
            data = int(input("Data 입력 : "))
            que.enqueue(data)
            que.printQueue()
        elif n == 2:
            que.dequeue()
            que.printQueue()
        elif n == 3:
            print("Queue size = ",que.qSize())
        elif n == 4:
            print("Empty? = ",que.isEmpty())
        elif n == 5:
            que.printQueue()
        elif n == 6:
            break
```
</div></details><br><br><br><br>

## 4. Priority 큐(우선순위 큐)

- 비 선형 자료구조로, 힙(Heap)을 통해 구현할 수 있다.
- 들어온 순서와 상관없이 우선순위가 가장 높은 Data가 출력됨.
- 최대, 최소값을 찾는 경우 많이 이용됨.
<br><br>

#### 4-1. 배열을 이용한 우선순위 큐
- 데이터 삽입/삭제 과정에서 데이터를 한 칸씩 당기거나 밀어야 하는 연산을 계속해야 하기 때문에 비효율적임.
- 삽입의 위치를 찾기 위해 배열에 저장된 모든 Data와 우선순위를 비교해야함.
<br><br>

#### 4-2. 연결리스트를 이용한 우선순위 큐
- 배열과는 다르게 Data를 밀거나 당겨줄 필요가 없음.
- 데이터가 많아지면 삽입/삭제 시 정렬(경쟁)을 할때 노드의 수에 비례해서 비교할 대상이 증가한다.
<br><br>

#### 4-3. 힙(연결리스트)으로 구현한 우선순위 큐
- 삽입/삭제 시 정렬(경쟁)을 할 때 비교 대상을 찾는 탐색시간이 노드 수에 비례해서 커진다.
  - 연결리스트 이기 때문에 처음 노드부터 비교 대상의 노드까지 탐색해야한다.
  - 이런 이유 때문에 더 간단한 배열로 구현한다.
<br><br>

#### 4-4. 힙(배열)으로 구현한 우선순위 큐
- 연결리스트와는 다르게 비교대상의 접근이 쉽기 때문에, 정렬(경쟁)하는 시간이 적다.
<br><br>

### 4-5. 복잡도 비교
- 배열 / 연결리스트
  - 정렬된 배열의 경우(삽입할 요소의 우선순위를 비교하면서 삽입해야함)
    - 삽입 O(N), 삭제 O(1)
  - 정렬되지 않은 배열의 경우(마지막 요소의 그냥 넣지만 삭제할 때 모든 원소와 우선순위를 따진다)
    - 삽입 O(1), 삭제 O(N)

- 힙(배열)
  - 삽입 / 삭제 : O(log N)  

<br>
<details>
<summary><font size = "5em" color = "red">queue 모듈을 사용한 우선순위 큐 구현</font></summary>
<div markdown = "1"> 
<br>

```python
from queue import PriorityQueue

# 우선순위 큐는 인덱스로 접근이 불가능하고, iterable하지 않기 때문에 for 문에서 iter로도 원소에 접근 불가능.
que = PriorityQueue()

que.put(4)
que.put(1)
que.put(7)
que.put(3)

print(que.get())
>> 1 
# 우선순위를 정해주지 않을 시 오름차순으로 return 


que.put((3,1))
que.put((5,2))
que.put((1,0))

print(que.get()[1])
>> 0
# (우선순위, value) 형태의 튜플로 넣는다.
```
</div></details><br>

<details>
<summary><font size = "5em" color = "red">heapq 모듈을 사용한 우선순위 큐 구현</font></summary>
<div markdown = "1"> 

<br>
- heapq모듈을 사용해 list를 최소 heap으로하는 heap으로 만듬.
<br>

```python
import heapq

heap = []
heapq.heappush(heap,(2,"minju"))
heapq.heappush(heap,(6,"junza"))
heapq.heappush(heap,(1,"sangwoo"))

# queue모듈의 PriorityQueue와 동일하게 튜플형식으로 push
print(heap)
>> [(1, 'sangwoo'), (6, 'junza'), (2, 'minju')]

# 최소 heap이기 때문에 우선순위의 값이 가장 낮은 Data부터 뽑아온다.
print(heapq.heappop(heap))
>> (1, 'sangwoo')
```
</div></details>
