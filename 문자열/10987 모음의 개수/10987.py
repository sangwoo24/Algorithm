import sys
st = sys.stdin.readline().strip()

count = 0

for i in range(len(st)):
    if st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u':
        count += 1

print(count)