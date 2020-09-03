n,l= map(int,input().split()) #4 2

a = list(map(int,input().split()))
a.sort() # 1 3 4 7

cnt = 1
num = a[0] + l #3

for k in range(1,len(a)):
    if a[k]+1 > num:
        cnt += 1
        num = a[k]+l
print(cnt)
        
        
    
