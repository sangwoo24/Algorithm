from itertools import permutations, combinations
def solution(numbers):
    s = []
    ans = []
    per = list(combinations(numbers,2))
    print(per)
    for i in range(len(per)):
        s.append(sum(per[i]))
    s = sorted(s)
    #1 1 2 3 3 4 5          #1 
    for i in range(len(s)):
        if i != 0:
            if s[i] != s[i-1]:
                ans.append(s[i])
        else:
            ans.append(s[i])
    return ans
#set형으로 변경하면 index 랜덤, -> 다시 오름차순으로 바꿔야함.