def solution(s):
    ans = ''
    index = 0
    for i in range(len(s)):
        if s[i] != " ":
            if index % 2 == 0:
                ans += s[i].upper()
            else:
                ans += s[i].lower()
            index += 1
        else:
            ans += s[i]
            index = 0
        
    return (ans)