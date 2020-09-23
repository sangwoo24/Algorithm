def solution(progresses, speeds):
    remain_time = []
    ans = []
    for i in range(len(progresses)):
        days = (100 - progresses[i]) % speeds[i]
        if days != 0:
            days = ((100 - progresses[i]) // speeds[i]) + 1
        else:
            days = (100 - progresses[i]) // speeds[i]
        remain_time.append(days)
    
    front = 0
    for idx in range(len(remain_time)):
        if remain_time[front] < remain_time[idx]:
            ans.append(idx - front)
            front = idx
    
    ans.append(len(remain_time) - front)
    return ans