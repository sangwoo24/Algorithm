num = [0 for _ in range(10)]
cnt = 0
str = input()

for i in range(len(str)):
    num[ord(str[i])-48] += 1

sn = num[6] + num[9]
num[6] = 0
num[9] = 0

if max(num) > 0:
    cnt += max(num)
    if sn > (cnt * 2):
        if (sn - (2*cnt)) % 2 == 0:
            cnt += (sn - (2*cnt)) % 2
        else:
            cnt += (sn - (2*cnt)) / 2 + 1
elif max(num) == 0:
    if sn % 2 == 0:
        cnt += sn / 2
    else:
        cnt += sn/2 + 1
print(int(cnt))



