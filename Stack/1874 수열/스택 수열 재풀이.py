import sys
from collections import deque

n = int(sys.stdin.readline())
def solution(n):
    num,ans,stack = [],[],[]
    m_index = 0
    for i in range(n):
        num.append(int(sys.stdin.readline()))

        if num[i] > m_index:
            for j in range(m_index,num[i]):
                ans.append("+")
                stack.append(j + 1)
            m_index = num[i]
        
        if stack[-1] == num[i]:
            stack.pop()
            ans.append("-")
        else:
            print("NO")
            return False
    for i in ans:
        print(i)
    return True

solution(n)