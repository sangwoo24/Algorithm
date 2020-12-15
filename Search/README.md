# Search [탐색]
----

## Linear Search [선형 탐색]
- ### 일치하는 항목을 찾거나 모든 요소를 확인 할 때까지 목록의 각 요소들을 하나씩 확인하는 탐색 알고리즘

- ### 장점
    - 가장 간단하고 직관적인 방법
- ### 단점
    - 최악의 경우 배열 전체를 탐색한다
- ### 복잡도
    - O(n)
<br><br>

## Binary Search [이진 탐색]
- ### 선형 탐색의 느린 탐색을 보안한 방법으로 배열의 중간 값을 비교해 절반을 제외 시키는 방법의 탐색 알고리즘

- ### 장점
    - 선형 탐색과 비교하여 탐색 시간이 빠르다
- ### 단점
    - 정렬 된 데이터에서만 사용할 수 있다.

- #### 복잡도
    - O(log n)
<br><br>

## BFS(너비 우선 탐색)
- ### 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 탐색 알고리즘


- ### 특징
    - BFS는 재귀적으로 동작하지 않는다
    - FIFO방식인 Queue를 사용한다
    - 두 노드 사이의 최단 경로를 찾을 때 사용한다
    - 프림, 다익스트라 알고리즘과 유사하다
- ### 장점
    - 너비를 우선으로 탐색하기 때문에, 경로가 여러 개인 경우에도 최단경로를 찾을 수 있다
    - 노드의 수가 적고 깊이가 얕은 해가 존재할 때 유리하다
- ### 단점
    - `재귀호출` 을 사용하는 `DFS` 와는 달리 큐를 이용하여 다음에 탐색할 노드들을 저장하기 때문에 노드의 수가 많을수록 더 큰 저장공간이 필요하다

### 1. 구현순서
- visited_queue(방문한 Node에 대한 list)
- need_visit_queue(방문해야 할 Node에 대한 list)
- graph dictionary(Key :각 Node Value : Node에서 뻗어나가는 인접한 Node)

### 2. 실행 순서
1. dictionary에 Key를 need_visit_queue에 push [최상위 Node부터 시작]
2. need_visit_queue에 push된 Key값을 빼서 visited_queue에 존재하는지 확인한다.
3. 존재한다면 넘어가고, 존재하지 않는다면 visited_queue에 key값을 넣어준다.
4. Key를 제외한 나머지 value값들을 need_visit_queue에 넣는다.
5. 1 ~ 4번과 동일한 방법으로 need_visit_queue에 있는 원소들을 하나씩 pop하여 visited_queue의 원소들과 대조시켜 판별한다.
<br><br>




## DFS(깊이 우선 탐색)
- ### 임의의 노드에서 시작해 다음 분기(Branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

 
- ### 특징
    - `Stack` 또는 `재귀함수` 로 구현한다.

- ### 장점
    - BFS에 비해 저장공간의 필요성이 적다. 백트래킹을 해야하는 노드들만 저장해주면 된다.
    - 찾아야 하는 노드가 깊은 단계에 있을수록, BFS보다 유리하다
    - BFS보다 좀 더 간단하게 구현 가능하다

- ### 단점
    - 단순 검색 속도 자체는 BFS에 비해서 느리다. 

### 1. 구현 순서
- visited_queue
- need_visit_stack(맨 하위노드로 갔다가 다시 위로 올라오기 위해 stack사용)
- graph dictionary
  
### 실행 순서
1. 초기 Node를 need_visit_stack에 넣고 하나씩 pop하여 visited_queue의 원소와 비교해서 넣거나 아무것도 하지않는다.
2. DFS는 queue가 아닌 스택이므로 가장 나중에 push된 원소가 빠져서 visited_queue의 원소와 비교된다. [stack : LIFO, queue : FIFO]



## DFS, BFS 시간복잡도 
- O(V + N) = O(간선 수 + 노드 수)