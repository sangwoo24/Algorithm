import math
num = [0 for _ in range(10)]

n = list(map(int,str(input())))

for i in n:
    num[i] += 1
num[6] += num[9]
num[9] = 0

if num[6] != 0:
    num[6] /= 2
print(math.ceil(max(num)))