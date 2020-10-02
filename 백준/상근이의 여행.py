import sys

T = int(input())

for i in range(T):
    N, M = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        a, b = list(map(int,sys.stdin.readline().split()))

    print(N-1)

