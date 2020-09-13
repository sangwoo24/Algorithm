import sys

n = int(sys.stdin.readline())
count = 0
fee = [500,100,50,10]

for i in fee:
    count += n // i
    n %= i
print(count)

# n을 10, 50, 100, 500의 4가지 숫자로 만들수 있는 최소 횟수 count 구하기

