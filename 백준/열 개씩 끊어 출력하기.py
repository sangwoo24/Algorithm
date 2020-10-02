s = input()
l = len(s)
ans = ''
for i in range(l):
    if i % 10 == 0 and i != 0:
        ans += '\n' + s[i]
    else:
        ans += s[i]
print(ans)