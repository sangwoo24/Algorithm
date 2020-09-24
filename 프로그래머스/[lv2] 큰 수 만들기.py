def solution(s, k):
    stack = [s[0]]
    for i in range(1,len(s)):
        while k > 0 and len(stack) > 0 and stack[-1] < s[i]:
            stack.pop()
            k -= 1
        stack.append(s[i])
    
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)