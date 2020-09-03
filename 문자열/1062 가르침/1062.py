import sys
from itertools import combinations

w = []              
ans = 0
ch = set()
teached = set("antic")            #teached = {'a','n','t','i','c'}

n,k = list(map(int,sys.stdin.readline().split())) #list 안붙혔을 경우 시간초과 뜸 why?

if k < 5:
    print(0)
    sys.exit()
if k == 26:
    print(n)
    sys.exit()
for i in range(n):
    st = sys.stdin.readline().rstrip()
    st = set(st[4 : -4]) - teached      # anti, tica 빼고 나머지 set으로 
    ch |= st                            # ch에 나버지 set 넣기 
    w.append(st)

candi = combinations(ch,min(len(ch),k - 5))  # candi에는 모든 조합이 들어감 -> min(k-5,len(ch))로 조합의 최소 갯수 구한 뒤 조합구함.

for i in candi:
    cnt = 0
    i = set(i)                               # candi(조합) 원소와 각 문자마다의 나머지 set을 비교해 
    for j in w:                              # 같으면 count++
        if len(j - i) == 0:                  # 다른 조합으로 더 많은 갯수의 문자를 찾을 수 있으므로 max로 ans값을 구해야함.
            cnt += 1
    ans = max(cnt, ans)

print(ans)
