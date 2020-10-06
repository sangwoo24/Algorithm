def solution(b, y):
    s = set()
    for i in range(1,(b+y) // 2):
        if (b+y) % i == 0 and (b+y)//i >= i and i >= 3:
            if (y % (i-2)) == 0 and (y // (i-2)) + 2 <= (b+y)//i:
                 if (((b+y)//i) - (y //(i-2))) % 2 == 0:
                    s.add(((b+y)//i,i))
    return (list(list(s)[0]))