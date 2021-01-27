#  Hash Table
---
## [key, value]로 데이터를 하고, 빠르게 데이터를 검색할 수 있는 자료구조

## 특징
- Python에서는 hash함수를 이용해 Key값을 받아오고, 그 Key값을 특정 길이로 mod연산을 하게되면 index를 만들 수 있다.
- Hash Table의 크기를 미리 지정하여 사용한다.
- 내부적으로 배열(버킷)을 사용하여 데이터를 저장하기 때문에 빠른 검색속도를 제공
- 각각의 Key값에 `해시함수` 를 적용해 고유한 index를 생성하여 사용함

## 활용
- 데이터 관리
- 캐싱


### 장점 
- 자료의 검색, 삽입, 삭제가 빈번한 경우에 용이
- Hash Key에 대한 Data가 중복인지 확인하기 쉽다.

### 단점
- 공간복잡도가 늘어난다. 속도를 늘리기 위해서 메모리를 더 많이 쓰는 자료구조
- Hash Key에 대한 index가 중복될 경우 충돌이 생긴다.

### 복잡도
- 저장/검색/삭제 : O(1)
- 최악의 경우, Collision이 발생하면 모든 버킷의 value를 찾아봐야 하는 경우가 발생하여 최대 O(n)의 복잡도가 될 수 있다.
<br><br>

## Hash Function [Hash Method]
- ### Data의 Key값을 고유한 index로 만들어주는 함수

- ### 특징
    - 이 메소드에 의해 반환된 데이터의 고유 숫자 값을 `hashcode` 라고 한다.
    - 메소드를 통해 key값을 `작은 범위의 값` 으로 바꿔준다.

<br><br>

## Collision [충돌]
  - ### 서로 다른 두 개의 Key가 같은 index로 hasing되면 충돌하여 같은 곳에 저장할 수 없게 되는 현상
  
    ### 1. Open Address 방식 (개방 주소법)
      > Collision이 발생하면, 다른 hash 버킷에 해당 자료를 삽입하는 방식 
      > 최악의 경우, 비어있는 버킷을 찾지 못해 탐색을 시작한 위치까지 되돌아올 수 있다.

      - #### Linear Probing : 순차적으로 탐색하며 비어있는 버킷을 찾을 때 까지 계속 진행된다.
      - #### Quadratic Probing : 2차 함수를 이용해 탐색할 위치를 찾는다.
      - #### Double Hasing Probing : 하나의 해쉬 함수에서 충돌이 발생하면 2차 Hash Function을 이용해 새로운 주소를 할당한다. 이는 많은 연산량이 요구된다
    <br>
    
    ### 2. Separate Chaining 방식 (분리 연결법)
      > Collision이 일어나면 해당 버킷을 확장시켜 데이터를 추가시키는 방식

      - #### Linked List : 버킷을 연결 리스트로 만들어 Collision이 일어나면 해당 버킷의 list에 추가하는 방식. 
      - #### Tree : 기본적인 알고리즘은 동일하지만, 버킷을 Tree 형태로 만든 방식.

<br><br>

    
## 1.기본 HashMap 생성
```python
import numpy as np

class HashMap():
    def __init__(self):
        self.table = np.empty(10,dtype = object)
        #numpy형식의 list 생성

    def get_hash_value(self,data):
        return hash(data)
        #hash함수를 사용해 key를 일정 길이의 정수로 반환 

    def hash_function(self,key):
        return key % 10
        #배열 크기에 맞는 hash_address로 변환하기 위한 작업

    def storage_data(self,key,data):
        hash_data = self.get_hash_value(key)
        hash_address = self.hash_function(hash_data)
        self.table[hash_address] = data
        #key에 해당하는 hash_address를 받아 Table에 저장 

    def find_data(self,key):
        hash_data = self.get_hash_value(key)
        hash_address = self.hash_function(hash_data)
        return self.table[hash_address]
```
  
## 2.HashTable의 충돌방지인 Chaining 기법
```python
import numpy as np

class HashMap():
    def __init__(self):
        self.table = np.empty(10,dtype = object)
    
    def get_key(self,data):
        return hash(data)

    def hash_function(self,key):
        return key % 10
    
    def storage_data(self,data,value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        
        if self.table[hash_address] != None:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == index_key:
                    self.table[hash_address][index][1] = value
                    return
            self.table[hash_address].append([index_key,value])
        else:
            self.table[hash_address] = [[index_key,value]]
    
    def get_data(self,data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)

        if self.table[hash_address] != None:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == index_key:
                    return self.table[hash_address][index][1]
            return None
        else:
            return None
```
- key와 value는 list형태로 table에 저장된다.
- 만일 key는 다르지만 동일한 hash_address가 생성될 경우에는 해당 hash_address에 존재하는 list뒤에 Linked List로 연결시켜준다.
- HashTable 외부의 공간을 생성하므로 공간복잡도는 증가한다.


## 3. HashTable의 충돌방지인 Linear Probing 기법



```python
import numpy as np

class HashMap():
    def __init__(self):
        self.table = np.empty(10,dtype = object)
    
    def get_key(self,data):
        return hash(data)

    def hash_function(self,key):
        return key % 10

    def storage_data(self,data,value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        
        if self.table[hash_address] != None:
            for index in range(hash_address,len(self.table)): #현재의 address부터 빈 공간이 있는지 확인하기 위해 
                if self.table[index] == None:
                    self.table[index] = [index_key,value] #각 table의 원소는 hash key와 value로 저장됨
                elif self.table[index][0] == index_key:
                    self.table[index][1] = value
                    return
        else:
            self.table[hash_address] = [index,value]

    def get_data(self,data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)

        if self.table[hash_address] != None:
            for index in range(hash_address,len(self.table)): 
                if self.table[index] == None:
                    return None:
                elif self.table[index][0] == index_key:
                    return self.table[index][1]
        else:
            return None
```

- Linear Probing 기법은 충돌 시 address앞의 빈공간에 key와 value를 넣으므로 data를 읽을 때 hash_address이후의 data를 순회하면서 자신이 원하는 key값이 있는지 확인해야한다.
- Linear Probing 기법은 동일한 Hash_Address일 경우 충돌 시 바로 다음칸이나 더 뒤의칸의 공백에 data가 들어가야하는데, 같은 hash_address를 가질경우 순회하면서 공백이 발견됐다는 것은 해당하는 index_key의 value가 저장된 적이 없다는 소리임.
