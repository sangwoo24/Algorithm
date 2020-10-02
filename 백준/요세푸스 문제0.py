from collections import deque as d
import sys
'''
n,k = map(int,sys.stdin.readline().split())

lst = [i+1 for i in range(n)]
ans = []
cnt = 0
i = 0

while lst:
    if cnt < k-1:
        cnt += 1
        i += 1
        if i >= len(lst):
            i -= len(lst)
        continue
    else:
        if len(lst) == 1:
            ans.append(str(lst.pop()))
        else:
            ans.append(str(lst.pop(i)))
        cnt = 0
    
print("<" + ', '.join(ans) + ">")
'''

n, k = map(int,sys.stdin.readline().split())
lst = d([i+1 for i in range(n)])
ans = []
cnt = 0

while lst:
    if cnt < k-1:
        lst.rotate(-1)
        cnt += 1
    else:
        ans.append(str(lst.popleft()))
        cnt = 0

print("<" + ', '.join(ans) + ">")

