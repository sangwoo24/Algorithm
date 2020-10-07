from queue import PriorityQueue

# 우선순위 큐는 인덱스로 접근이 불가능하고, iterable하지 않기 때문에 for 문에서 iter로도 원소에 접근 불가능.
que = PriorityQueue()

que.put(4)
que.put(1)
que.put(7)
que.put(3)

print(que.get())
# >> 오름차순으로 return


que.put((3,1))
que.put((5,2))
que.put((1,0))

print(que.get()[1])