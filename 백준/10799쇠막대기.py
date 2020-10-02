import sys

s = sys.stdin.readline().strip()
ans = 0
iron_bar = 0

for i in range(len(s)):
    if s[i] == "(":
        iron_bar += 1
    else:
        iron_bar -= 1
        if s[i-1] == "(":
            ans += iron_bar
        else:
            ans += 1
print(ans)

