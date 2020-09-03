n,m = map(int,input().split())
s = 1

if n == 1:
    s = 1
elif n == 2:
    s = min(4,int((m+1)/2))
elif n > 2:
    if m < 7:
        s = min(4,m)
    elif m >= 7:
        s = m-2
print(s)
