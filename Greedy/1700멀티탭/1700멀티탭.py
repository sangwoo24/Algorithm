n,k  = map(int,input().split())
num = list(map(int,input().split()))
lam = 0
idx = 0
plug = [0 for i in range(n)]

for i in range(k):
    flag = 0
    for j in range(n):
<<<<<<< HEAD:Greedy/1700멀티탭/1700멀티탭.py
        if num[i] == plug[j]:
            flag = True
    if flag:
        continue

    for j in range(n):
        if plug[j] == 0:
            plug[j] = num[i]
            flag = True
            break

    if flag:
=======
        if plug[j] == num[i]:
            flag = 1

    if flag == 1:
        continue
    
    for j in range(n):
        if plug[j] == 0:
            plug[j] = num[i]
            flag = 1
            break

    if flag == 1:
>>>>>>> 3a601f02fa630ba3cc6ad3e3dee2d5f65a01a047:Greedy/1700멀티탭/1700멀티탭.py
        continue

    m = -1

    for z in range(n):
        cnt = 0
        for p in range(i+1,k):
            if plug[z] == num[p]:
                break
            else:
                cnt += 1

        if cnt > m:
            m = cnt
            idx = z
    lam += 1
    plug[idx] = num[i]
    idx = 0
print(lam)

    


    
        
    
