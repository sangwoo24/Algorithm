from itertools import combinations
import sys
#걸린 시간 : 15분

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def solution(n,m,arr):
    com = list(combinations(arr,3))

    num = 0
    for i in range(len(com)):
        if sum(com[i]) <= m:
            if sum(com[i]) > num:
                num = sum(com[i])
    return num


print(solution(n,m,arr))
