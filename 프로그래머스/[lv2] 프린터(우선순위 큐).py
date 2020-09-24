from collections import deque

def solution(p,l):
    printer = deque([p[i],i] for i in range(len(p)))
    cnt = 0
    while True:
        if printer[0][0] < max(p):
            printer.rotate(-1)
        elif printer[0][0] >= max(p):
            if printer[0][1] == l:
                break
            else:
                p[printer[0][1]] = 0
                printer.popleft()
    return p.count(0) + 1