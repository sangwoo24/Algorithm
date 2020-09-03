def root():
    n = int(input())
    a = [[0] * n for i in range(n)]
    checker = [[0] * n for i in range(n)]
    
    for i in range(n):
        line = input().split()
        for j in range(n):
            a[i][j] = int(line[j])


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue

                if a[i][j] > a[i][k] + a[k][j]:
                    print(-1)
                    return

                if a[i][j] == a[i][k] + a[k][j]:
                    checker[i][j] = 0

    total_sum = 0
    for i in range(n):
        for j in range(n):
            if checker[i][j] == 1:
                total_sum += a[i][j]

    print(total_sum//2)
    
root()

