import sys

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