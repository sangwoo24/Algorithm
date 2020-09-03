import sys

n = int(sys.stdin.readline())
cnt = 0


for i in range(n):
    flag = 0
    alpa = [0 for k in range(26)]

    str = input()

    for j in range(len(str)):

        if j >= 1:
            if str[j] != str[j-1]:
                if alpa[ord(str[j])-97] == 1:
                    flag = 1
                    break
        alpa[ord(str[j]) - 97] = 1

    if flag == 0:
        cnt += 1
print(cnt)
