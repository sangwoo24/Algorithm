import sys
import time

#n에서 1을 빼거나 k로 나눠서 1을 만들 수 있는 최소 횟수

def one():
    n,k = map(int,sys.stdin.readline().split())

    count = 0
    if n == 1:
        return 0

    while n != 1:
        if n % k != 0:
            n -= 1
        else:
            n = n // k 
        count += 1
    return count

def mul_or_add():
    result = 0
    s = sys.stdin.readline()

    num = int(s[0])
    for i in range(1,len(s)-1):
        if int(s[i]) <= 1 or num <= 1:
            num += int(s[i])
        else:
            num *= int(s[i])
    print(num)


if __name__ == "__main__":
    mul_or_add()


