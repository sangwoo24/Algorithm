import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().strip()
    stack_a = []
    stack_b = []
    for j in range(len(s)):
        if s[j] == "<":
            if len(stack_b) != 0:
                stack_a.append(stack_b.pop())
        elif s[j] == ">":
            if len(stack_a) != 0:
                stack_b.append(stack_a.pop())
        elif s[j] == "-":
            if len(stack_b) != 0:
                stack_b.pop()
        else:
            stack_b.append(s[j])
    for j in range(len(stack_a)):
        stack_b.append(stack_a.pop())
    print(''.join(stack_b))