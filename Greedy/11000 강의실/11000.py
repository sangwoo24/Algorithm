import sys
from queue import PriorityQueue

que = PriorityQueue()

n = int(sys.stdin.readline())

a = []
for i in range(n):
    s,t = map(int,sys.stdin.readline().split())
    lst = []
    lst.extend([s,t])
    a.append(lst)

a.sort(key = lambda x : x[0])

que.put(a[0][1])


for i in range(1,n):
    if que.queue[0] <= a[i][0]:
        que.get()
        que.put(a[i][1])
    else:
        que.put(a[i][1])
print(que.qsize())


