# QUEUE
<br>



<br><br>

## - 특징 
- 선형 자료구조의 일종으로 먼저 넣은 데이터가 먼저 나오는 FIFO(First In First Out) 구조입니다.
- 큐에 새로운 Data가 들어오면 enqueue를, Data가 삭제될 때는 dequeue를 수행합니다.
- 주로 컴퓨터 버퍼에 사용되며 입력이 초과되어 작업을 진행하지 못할 시, 버퍼(큐)를 만들어서 대기시킨 후 추후에 순차적으로 작업을 진행시킵니다.
- 데이터를 추가한 순서대로 제어할 수 있기 때문에 스트리밍(Streaming), 너비 우선 탐색(BFS), 프로세스 스케줄링 등 에서 사용됩니다.

<br>

## - 큐의 종류
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

<details>
<summary>1-1. 선형 큐 구현</summary>
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
<br>

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

## 2. 원형큐
<center><img width="408" alt="스크린샷 2020-10-07 오후 5 43 40" src="https://user-images.githubusercontent.com/56511253/95308266-a59bde80-08c4-11eb-89f5-6134d1ff3b32.png"></center>

- 선형 큐와 동일하게 1차원 배열을 이용하지만 처음과 끝이 원형처럼 이어져 있다고 가정합니다.
- 큐를 원형으로 생각해야하기 때문에 mod연산을 사용해야합니다.
- 선형 큐에서는 필요했던, 삭제 시 데이터들을 한번씩 앞당겨주는 불필요한 작업들을 없앨 수 있다.

<details>
<summary>원형 큐 구현</summary>
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
</div></details>