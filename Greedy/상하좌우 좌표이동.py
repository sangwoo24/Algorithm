import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().split())
cordinates = [[-1,0],[1,0],[0,-1],[0,1]]
direction = ['L','R','U','D']

x, y = 1, 1
for i in range(len(s)):
    for j in range(len(direction)):
        if s[i] == direction[j]:
            dx = x + cordinates[j][0]
            dy = y + cordinates[j][1]
    
    if dx < 1 or dy < 1 or dx > n or dy > n:
        continue
    
    x, y = dx, dy 

print(x,y)


