import sys

N = (int)(sys.stdin.readline())
count = 0

for i in range(N):
    word = list(sys.stdin.readline().strip())
    s = []
    for j in range(len(word)):
        if not s:
            s.append(word[j])
        else:
            if s[-1] == word[j]:
                s.pop()
            else:
                s.append(word[j])
    if not s:
        count += 1
print(count)