def solution(x):
    sum = 0
    n = x
    while x // 10 > 0:
        sum += (x % 10)
        x //= 10
    if n % (sum + x) == 0:
        return True
    else:
        return False

# 풀이 2
'''
def solution(x):
    sum = 0
    for i in range(len(str(x))):
        sum += int(str(x)[i])
    if x % (sum) == 0:
        return True
    else:
        return False
'''