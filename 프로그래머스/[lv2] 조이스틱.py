def solution(name):
    ans = []
    for i in name:
        a = ord(i) - 65
        b = 91 - ord(i)
        ans.append(a if a < b else b)
        
    num = ans[0]
    ans[0] = 0
    idx = 0
    while ans.count(0) != len(ans):
        left_cnt = 0
        right_cnt = 0
        while True:
            left_cnt -= 1
            if ans[idx + left_cnt] != 0:
                break
        while True:
            right_cnt += 1
            if ans[idx + right_cnt] != 0:
                break
        if right_cnt < (-left_cnt) or right_cnt == (-left_cnt):
            num += ans[idx + right_cnt] + right_cnt
            ans[idx + right_cnt] = 0
            idx += right_cnt
        elif right_cnt > (-left_cnt):
            num += ans[idx + left_cnt] + (-left_cnt)
            ans[idx + left_cnt] = 0
            idx += left_cnt
        
    return (num)

    