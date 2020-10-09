def solution(s):
    stack = []
    
    for i in range(len(s)):
        if i == 0 and s[i] == ")":
            return False
        
        if stack:
            if s[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if stack:
        return False
    else:
        return True