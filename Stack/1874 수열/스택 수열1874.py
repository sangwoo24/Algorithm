import sys

n = int(sys.stdin.readline())
num = 1
flag = 0
home = []
stack = []
ans = []
for i in range(n):
    k = int(sys.stdin.readline())
    home.append(k)

for i in range(n):
    if len(stack) == 0 or home[i] > stack[-1]:
        while num <= home[i]:
            stack.append(num)
            num += 1
            #print("+")
            ans.append("+")

    if stack[-1] == home[i]:
        stack.pop()
        #print("-")
        ans.append("-")

    elif stack[-1] > home[i]:
        flag = 1

if flag:
    print("NO")
else:
    for i in ans:
        print(i)


