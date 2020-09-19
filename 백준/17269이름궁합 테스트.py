import sys
n, m = map(int,sys.stdin.readline().split())
s1, s2 = map(str,sys.stdin.readline().split())

num = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
ans = []

s = ''
for i in range(min(n,m)):
    ans.append(num[ord(s1[i])-65])
    ans.append(num[ord(s2[i])-65])

if n > m:
    for i in range(m,len(s1)):
        ans.append(num[ord(s1[i])-65])
else:
    for i in range(n,len(s2)):
        ans.append(num[ord(s2[i])-65])

while True:
    ret = []
    for i in range(1, len(ans)):
        if ans[i] + ans[i-1] >= 10:
            ret.append((ans[i] + ans[i-1]) % 10)
        else:
            ret.append(ans[i] + ans[i-1])
    ans = ret
    if len(ret) == 2:
        break
for i in range(len(ret)):
    if i == 0 and ret[i] == 0:
        continue
    s += str(ret[i])
print(s + "%")