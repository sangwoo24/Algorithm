import sys
try:
    n = int(sys.stdin.readline())
except: exit()

cnt = [0 for i in range(n)]
a = []
for i in range(n):
    try:
        day = list(map(int,input().split()))
    except: exit()
    a.append(day)

a = sorted(a, key = lambda x : x[1],reverse = True)
s = 0
for i in range(n):
    for j in range(a[i][0],0,-1):
        if cnt[j-1] == 0:
            cnt[j-1] = 1
            s += a[i][1]
            break
print(s)
