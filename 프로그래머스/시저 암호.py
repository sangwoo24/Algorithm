def solution(s, n):
    lst = list(s)
    #90 122
    for i in range(len(lst)):
        if lst[i].isupper():
            if ord(lst[i]) + (n % 26) > 90:
                lst[i] = chr(ord(lst[i]) + (n % 26) - 26)
            else:
                lst[i] = chr(ord(lst[i]) + (n % 26))
        elif lst[i].islower():
            if ord(lst[i]) + (n % 26) > 122:
                lst[i] = chr(ord(lst[i]) + (n % 26) - 26)
            else:
                lst[i] = chr(ord(lst[i]) + (n % 26))
                    
    return ''.join(lst)