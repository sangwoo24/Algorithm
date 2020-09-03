n   = int(input())
num = list(map(int,input().split()))
arr = [0 for i in range(11)]

for i in range(n):
    b = num[i]
    for j in range(n):

        if b == 0 and arr[j] == 0:
            arr[j] = i+1
            break
            
        elif arr[j] == 0:
            b -= 1

for i in range(n):
    print(arr[i],end = ' ')
