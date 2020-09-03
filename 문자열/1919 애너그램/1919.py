import sys

count = 0
b = []
st = []

for i in range(2):
    b.append([0 for i in range(26)])

for i in range(2):
    st .append(list(sys.stdin.readline().strip()))

for i in range(2):
    for j in range(len(st[i])):
        b[i][ord(st[i][j]) - 97] += 1

for i in range(26):
    if b[0][i] != b[1][i]:
        count += abs(b[0][i] - b[1][i])
print(count)