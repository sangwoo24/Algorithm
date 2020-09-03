import sys

a = [0 for i in range(5)]

for i in range(5):
    st = sys.stdin.readline().strip()
    if "FBI" in st:
        a[i] += 1

if sum(a) == 0:
    print("HE GOT AWAY!")
else:
    for i in range(len(a)):
        if a[i] != 0:
            print(i+1, end = ' ')