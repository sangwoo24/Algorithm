from sys import stdin

alpa = [0] * 26
str = input()

for i in range(len(str)):
    alpa[ord(str[i]) - 97] += 1

for i in range(len(alpa)):
    print(alpa[i])
