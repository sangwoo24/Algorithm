from itertools import combinations

def solution(clothes):
    com = dict()
    ans = 1
    for i in range(len(clothes)):
        if clothes[i][1] in com:
            com[clothes[i][1]].append(clothes[i][0])
        else:
            com[clothes[i][1]] = [clothes[i][0]]

    for i in com.keys():
        ans *= len(com[i]) + 1
    return (ans-1)
    # for i in range(1,len(com.keys())+1):
    #     num = list(combinations(com.keys(),i)) 
    #     for j in range(len(num)):
    #         mul = 1
    #         for k in range(len(num[j])):
    #             mul *= len(com[num[j][k]])
    #         ans += mul
    # return (ans)