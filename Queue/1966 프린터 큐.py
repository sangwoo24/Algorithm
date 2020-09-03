import collections

case = int(input())

for i in range(case):
    cnt = 0
    flag = 0
    n,m = map(int,input().split())
    imp = list(map(int,input().split()))
    num = collections.deque([])
    for j in range(n):
        num.append([imp[j],j])
    #num[0][0] = 우선순위, num[0][1] = 순서
    while True:
        while num[0][0] < max(imp):
            num.rotate(-1)

        if num[0][1] != m:
            cnt += 1
            num.popleft()
            del imp[imp.index(max(imp))]
        else:
            #cnt += 1
            flag = 1
            break

    if flag:
        for k in range(len(imp)):
            if num[k][1] != m:
                cnt += 1
            else:
                cnt += 1
                break
    print(cnt)
