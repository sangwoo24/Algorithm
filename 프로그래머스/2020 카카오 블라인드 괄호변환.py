def divString(s):
    l = 0
    r = 0
    u = ""
    v = ""
    for i in range(len(s)):
        if s[i] == "(":
            l += 1
        else:
            r += 1
        
        if r == l:
            u = s[:i+1]
            v = s[i+1:]
            break
    return u,v

def isBracket(s):

    stack = []
    for i in range(len(s)):
        if s[i] == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        return True
    else:
        return False
    
def solution(p):
    ans = ""
    if isBracket(p) or p == "":
        return p
    
    u, v = divString(p)
    if isBracket(u): # U가 올바른 괄호 문자열이면
        return u + solution(v)#v에 과한것
    
    else:
        ans += "(" + solution(v) + ")"
        u = list(u)
        del u[0]
        del u[-1]
        for i in range(len(u)):
            if u[i] == "(":
                ans += ")"
            else:
                ans += "("
        return ans