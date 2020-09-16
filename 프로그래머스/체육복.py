'''
n = 학생 수 
lost = 잃어버린 학생 번호 
reserve = 여분의 체육복이 있는 학생


1 2 3 4
lost = [2,3]
reserve = [2,3] -> 4

lost = [2,3]  1 2 0 4
reserve = [1,2] -> 3
'''
'''
def solution(n, lost, reserve):
    stu = [i for i in range(1,n+1)]
   
    lost.sort()
    reserve.sort()

    for i in lost:
        if i not in reserve:
            stu[i - 1] = 0

    for res in reserve:
        if res not in lost:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            if res != n:
                if stu[res] == 0:
                    stu[res] = res + 1
                    continue
                if res >= 2:
                    if stu[res-2] == 0:
                        stu[res-2] = res - 1
            else:
                if stu[res-2] == 0:
                    stu[res-2] = res - 1
    answer = n - stu.count(0)
    return answer
'''
def solution(n, lost, reserve):
    stu = [i for i in range(1,n+1)]
   
    lost.sort()
    reserve.sort()

    for i in lost:
        if i not in reserve:
            stu[i - 1] = 0

    for res in reserve:
        if res not in lost:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            if res-1 != 0:
                if stu[res-2] == 0:
                    stu[res-2] = res - 1
                    continue
                if res != n:
                    if stu[res] == 0:
                        stu[res] = res + 1

    answer = n - stu.count(0)
    return answer

