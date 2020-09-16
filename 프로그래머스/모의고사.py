from collections import deque
#student = deque([[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]])


def solution(answers):
    student = [deque([1,2,3,4,5]),deque([2,1,2,3,2,4,2,5]),deque([3,3,1,1,2,2,4,4,5,5])]
    index_list = [0,0,0]
    answer = []

    for ans in answers:
        for i in range(len(index_list)):
            if ans == student[i][0]:
                index_list[i] += 1
            student[i].rotate(-1)

    m = max(index_list)
    return [i + 1 for i, v in enumerate(index_list) if v == m]


'''
    m = max(index_list)
    for i in range(len(index_list)):
        if index_list[i] == m:
            answer.append(i+1)
    return sorted(answer)
'''

a = [1,2,3,4,5]
print(solution(a))


