import sys

n = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
A = [B[0]]


for i in range(1,len(B)):
    A.append((B[i] * (i + 1)) - B[i-1] * i)

for i in range(len(A)):
    print(A[i], end = ' ')
