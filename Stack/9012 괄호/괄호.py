import sys

n = int(sys.stdin.readline())

for i in range(n):
    cnt = 0
    s = sys.stdin.readline()

    for j in range(len(s)):
        if s[j] == '(':
            cnt += 1
        elif s[j] == ')':
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
    
            
