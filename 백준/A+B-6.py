t = int(input())

for i in range(t):
    s = input()
    s = list(s.split(','))
    
    s = [int(j) for j in s]
    print(sum(s))
