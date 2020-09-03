import collections

n = int(input())

num = collections.deque([i for i in range(1,n+1)])
for i in range(n):

while len(num) > 1:
    num.popleft()
    num.rotate(-1)

print(num[0])
