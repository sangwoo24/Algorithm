import sys


if __name__ == "__main__":
    n = (int)(sys.stdin.readline())
    
    for i in range(n): 
        s = list(sys.stdin.readline().strip())
        if i == 0:
            check = s
        if i >= 1:
            for j in range(len(s)):
                if s[j] != check[j]:
                    check[j] = '?'
    r = "".join(check)
    print(r)
    

    
        
    