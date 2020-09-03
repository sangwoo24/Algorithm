import sys

st = list(sys.stdin.readline().strip())

joi = 0
ioi = 0

for i in range(len(st) - 2):
    if ''.join(st[i : i + 3]) == "JOI":
        joi += 1
    elif ''.join(st[i : i + 3]) == "IOI":
        ioi += 1

print(joi)
print(ioi)