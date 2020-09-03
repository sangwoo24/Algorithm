import sys
lst = []
for i in range(int(sys.stdin.readline())):
    num = float(sys.stdin.readline())

    if i < 6:
        lst.append(num)
        lst.sort()
    else:
        if lst[-1] > num:
            lst[-1] = num
            lst.sort()

for i in lst:
    print('%.3f' % i)