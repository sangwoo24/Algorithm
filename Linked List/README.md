# Linked List
---------
## 데이터와 포인터를 가지고 있는 `노드`가 한 줄로 연결되어 있는 방식의 자료구조.

## 특징
- 배열의 단점을 보완한 자료구조 
- 노드의 포인터는 이전과 다음의 데이터와 연결되어 있다.
- Python에는 List에서 Linked List 기능을 지원.
- 단일, 이중, 원형 연결리스트가 있다. 
- Tree 자료구조의 근간이 된다

## 장점
- 원하는 만큼 노드를 동적으로 추가/삭제 할 수 있다.

## 단점
- 배열처럼 메모리 공간에 정렬되어 있지 않고 사방에 흩어져있기 때문에 특정 노드에 바로 접근할 수 없다. (= 특정 노드를 찾기 위해서는 노드를 순회해야 한다)
  
## 복잡도
- 추가/삭제 : O(n)
- 검색 : O(n)
  
## 1. Linked List 생성
- Linked List를 만들기 위해서는 Data와 주소가 포함된 Node를 생성해야함.

```python
class Node():   
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
# Class를 만들고 Node의 객체를 생성해야 각 객체의 주소를 알 수 있음.
```
```python
class LinkedList():
    def __init__(self,data):
        firstNode = Node(data)
        self.head = firstNode
    
    #Linked list 맨 뒤 원소추가
    def append(self,data):
        new_node = Node(data)
        head = self.head
        if head == '':
            head = new_node
        while head.next:
            head = head.next
        head.next = new_node
```

## 1-1. Linked List 기능구현(원소삽입, 삭제, 특정원소 삽입 등)
```python
#특정 원소의 뒤에 새로운 원소 삽입
def insert(self,stored_data,new_data):
        new_node = Node(new_data)
        head = self.head

        while head.data != stored_data:
            head = head.next
            if head == None:
                print("찾는 원소가 없습니다")
                return False
        new_node.next = head.next
        head.next = new_node

    def print_linked_list(self):
        head = self.head
        while head:
            print("LinkedList에 존재하는 노드는 : ",head.data)
            head = head.next
    
    #Linked list 원소 삭제 
    def delete(self,data):
        head = self.head
        if head == '':
            print("삭제할 원소가 없습니다")
            return False
        if head.data == data:
            self.head = None
            del head
            return True
        
        while (head.next != None) and (head.next.data != data):
            head = head.next
            if head == None:
                print("찾는 원소가 없습니다")
        temp = head.next
        head.next = head.next.next
        del temp

```


## 2. Double Linked List 구현
- 다음 Node의 주소를 가리키는 next와 이전 원소의 주소를 가리키는 prev 두개로 구성된다.
  
## 2-1 Double Linked List 생성

```python
class Node():
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
```
```python
class DoubleLinkedList():
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    #Double Linked List 맨 앞부터 원소출력
    def print_list_front(self):
        head = self.head
        while head:
            print("맨 앞부터 List 원소 출력 : ",head.data,"-------Prev : ",head.prev, "Next : ",head.next)
            if head.prev != None:
                print("이전 data : ",head.prev.data)
            if head.next != None:
                print("앞 data : ", head.next.data)
            head = head.next
```
### 2-1 Double Linked List 기능구현

```python
def append(self,data):
        new_node = Node(data)
        head = self.head
        if head == '':
            head = new_node
        while head.next:
            head = head.next
        new_node.prev = head
        head.next = new_node
        self.tail = new_node
    
    #Double Linked List 특정 원소 뒤에 삽입
    def insert(self,stored_data,new_data):
        tail = self.tail

        while tail.data != stored_data:
            tail = tail.prev
            if tail == None:
                print("찾는 원소가 없음")
                return False
        new_node = Node(new_data)
        if tail.next != None:
            tail.next.prev = new_node
        else:
            self.tail = new_node
        new_node.next = tail.next
        tail.next = new_node
        new_node.prev = tail
    

    def delete(self,data):
        head = self.head

        if head == '':
            print("지울 노드가 없습니다")
            return False
        
        if head.data == data:
            self.head = head.next
            del head

        while head.data != data:
            head = head.next
            if head == None:
                print("찾는 원소가 없습니다")
                return False
        head.prev.next = head.next
        head.next.prev = head.prev
        del head

    def delete(self,data):
        head = self.head
        if head == '':
            print("삭제할 노드가 없습니다") 
            return False
        if head.data == data:
            self.head = head.next
            if head.next:
                head.next.prev = None
            del head
            return True
        while head.data != data:
            head = head.next

        if head.next == None:
            head.prev.next = head.next
        else:
            head.prev.next = head.next
            head.next.prev = head.prev
        del head
```

