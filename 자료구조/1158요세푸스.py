#queue 사용 시 일반 list로 할 경우 시간초과가 빈번히 발생.
#queue를 이용해 문제를 풀 땐 collections.deque를 사용하자.
'''
import sys
import collections

n, k = map(int,sys.stdin.readline().split())
num = collections.deque([i for i in range(1,n+1)])
permutation = []


for i in range(n):
    for j in range(k):
        num.append(num.popleft())
    permutation.append(num.pop())


print('<',end='')
for i in range(len(permutation) - 1):
    print('{}, '.format(permutation[i]),end='')
print(permutation[len(permutation) - 1],end ='')
print('>')
'''
import sys

n, k = map(int,sys.stdin.readline().split())
num = [i for i in range(1,n+1)]
ans = []
index = 0

while len(num) > 0:
    index += k - 1
    if index >= len(num):
        index %= len(num)
    ans.append(num.pop(index))

print(ans)
print('<' + ", ".join(map(str,ans)) + '>')