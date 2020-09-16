def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        per[x] = p

def union(x,y):
    x = find(x)
    y = find(y)

    if x !=y:
        parent[x] = y
        network_num[x] += network_num[y]

t = int(input())
network_num = dict()
parent = dict()
for _ in range(t):
    n = int(input())
    for _ in range(n):
        a,b = map(sys.stdin.readline().split())
        
        if a not in parent:
            parent[a] = a
            network_num[a] = 1
        if b not in parent:
            parent[b] = b
            network_num[b] = 1