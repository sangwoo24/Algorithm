import sys


a, b = map(int,sys.stdin.readline().split())

listen = set([sys.stdin.readline().strip() for i in range(a)])
see = set([sys.stdin.readline().strip() for i in range(b)])

intersection = sorted(list(listen & see))

print(len(intersection))
for i in intersection:
    print(i)
