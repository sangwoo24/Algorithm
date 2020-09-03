import sys

i = 1
while(1): 
    l,p,v = map(int,sys.stdin.readline().split())
    if l == p == v == 0:
        break;
    else:
        print("Case {} : {}".format(i,(int)(v/p)*l+l if v % p > l else (int)(v/p)*l + v%p))
    i += 1
    
