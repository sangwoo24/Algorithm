import sys
n = int(input())
lst = list(map(int,sys.stdin.readline().split()))
x = int(input())
ans = 0
cnt = [0 for i in range(2000000)]
start, end = 0, 0

while end < n-1:
    cnt[lst[start]] += 1
    end += 1
    ans += cnt[x-lst[end]]
    start += 1
print(ans)