n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in arr:
        print('1')
    else:
        print('0')