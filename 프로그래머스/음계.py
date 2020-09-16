import sys

n = list(map(int, sys.stdin.readline().split()))



def solution(n):
    if n[0] != 1 and n[0] != 8:
        return "mixed"
    
    if n[0] == 1:
        for i in range(1,len(n)):
            if n[i] != n[i-1] + 1:
                return "mixed"
        return "ascending"
    elif n[0] == 8:
        for i in range(1,len(n)):
            if n[i] != n[i-1] - 1:
                return "mixed"
        return "descending"


print(solution(n))