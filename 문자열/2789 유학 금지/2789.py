import sys

st = sys.stdin.readline().strip()
s = ""

for i in range(len(st)):
    if not(st[i] == 'C' or st[i] == 'A' or st[i] == 'M' or st[i] == 'B' or st[i] == 'R' or st[i] == 'I' or st[i] == 'D' or st[i] == 'G' or st[i] == 'E'):
        s += st[i]

print(s)

