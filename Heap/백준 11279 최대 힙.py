from collections import deque
import sys

n = map(int, sys.stdin.readline())
queue = deque([])

for i in range(n):
    num = int(input())
    if num != 0:
        queue.append(num)
    else:
        if queue:
            print(max(queue))
        else:
            print(0)


