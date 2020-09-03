import sys

N = (int)(sys.stdin.readline())

for _ in range(N):
    a, b = map(list,sys.stdin.readline().split())
    dis = []
    for i in range(len(a)):
        if a[i] <= b[i]:
            dis.append(ord(b[i]) - ord(a[i]))
        else:
            dis.append(26 - (ord(a[i])- ord(b[i])))
    print(f'Distances: {" ".join(str(i) for i in dis)}')
