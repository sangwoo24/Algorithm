def solution(n):
    subak = '수박'
    ans = ''
    index = 0
    for i in range(n):
        if index >= 2:
            index = 0
        ans += subak[index]
        index += 1
    return ans