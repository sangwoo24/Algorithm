import sys

s = list(sys.stdin.readline().rstrip())
result_str = []

result_num = 0
for i in range(len(s)):
    try:
        num = int(s[i])
        result_num += num
    except:
        result_str.append(s[i])

print(''.join(sorted(result_str)) + str(result_num))

