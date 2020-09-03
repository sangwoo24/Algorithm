import sys

conv = []
st = sys.stdin.readline().strip()

for i in range(len(st)):
    if ord(st[i]) >= 68:
        conv.append(chr(ord(st[i]) - 3))
    elif ord(st[i]) >= 65 and ord(st[i]) < 68:
        conv.append(chr(ord(st[i]) + 23))
print("".join(conv))
