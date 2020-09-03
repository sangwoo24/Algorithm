import sys

if __name__ == "__main__":
    count = 0
    flag = False
    for i in range(8):
        b = sys.stdin.readline()
        if i % 2 == 0:
            for j in range(4):
                if b[2 * j] == 'F':
                    count += 1
        elif i % 2 != 0:
            for j in range(4):
                if b[2 * j + 1] == 'F':
                    count += 1

    print(count)

# for문을 최대한 줄여야함.
# index를 활용해야함(mod, div)