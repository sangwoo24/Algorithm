def solution(s):
    m = 9999
    
    for i in range(1,(len(s)//2) + 1):
        ret = ''
        lst = []
        cnt = 1
        for j in range(0,len(s),i):
            if j == 0:
                ans = s[j:j+i]
            else:
                if ans == s[j:j+i]:
                    cnt += 1
                else:
                    if cnt > 1:
                        ret += str(cnt) + ans
                        cnt = 1
                    elif cnt == 1:
                        ret += ans
                ans = s[j:j+i]
        if cnt > 1:
            ret += str(cnt) + ans
        elif cnt == 1:
            ret += ans
        
        if len(ret) < m:
            m = len(ret)
    return len(s) if m == 9999 else m