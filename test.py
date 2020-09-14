#work = [93,30,55]
#time = [1,30,5]

work = [94,96,97,99,80]
time = [1,5,4,4,10] 

remain_time = []
ans = [0 for i in range(len(work))]
for i in range(len(work)):
    days = (100 - work[i]) % time[i]
    if days != 0:
        days = int(((100 - work[i]) // time[i])) + 1
    else:
        days = int((100 - work[i]) // time[i])
    remain_time.append(days)

num = remain_time[0]
cnt = 1
index = 0
ans[index] = cnt

for i in range(1,len(remain_time)):
    if num - remain_time[i] > 0:
        cnt += 1
        ans[index] = cnt
    else:
        cnt = 1
        index += 1
        ans[index] = cnt

print([i for i in ans if i != 0])