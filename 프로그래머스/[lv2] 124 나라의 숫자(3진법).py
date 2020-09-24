def solution(n):
    ans = ''
    
    while n:
        n, m = divmod(n,3)
        ans = "412"[m] + ans
        if m == 0:
            n -= 1
    return ans