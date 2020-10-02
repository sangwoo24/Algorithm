def solution(num):
    num.sort()
    index = 0
    for i in range(len(num)+1):
        cnt = 0
        for j in range(len(num)):
            if num[j] >= i:
                cnt = j
                break
        if len(num) - cnt >= i and num[cnt-1] <= i and cnt > 0:
            index = i
        elif cnt == 0:
            if num[0] >= len(num):
                index = len(num)
            else:
                index = min(num)
    return index