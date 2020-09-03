
n,l = map(int, input().split())

num = list(map(int,input().split()))
sum = 0
total = 0

for i in range(l,n+1):
    for j in range(6-i+1):
        for k in range(j,j+i):
            sum += num[k]
        sum /= i
        if total == 0:
            total = sum
        else:
            if sum < total:
                total = sum
        sum = 0

print(format(total,'.10f'))

