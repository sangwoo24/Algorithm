import sys

# sum = []
# a, b = map(int,sys.stdin.readline().split())
# sum.append(a + b)

# lstA = list(str(a))
# lstB = list(str(b))

# for i in range(len(lstA)):
#     if lstA[i] == '5':
#         lstA[i] = '6'
#     if lstB[i] == '5':
#         lstB[i] = '6'
# s = int("".join(lstA)) + int("".join(lstB))
# sum.append(s)
# for i in range(len(lstA)):
#     if lstA[i] == '6':
#         lstA[i] = '5'
#     if lstB[i] == '6':
#         lstB[i] = '5'
# s = int("".join(lstA)) + int("".join(lstB))
# sum.append(s)

# print(min(sum), max(sum))

#----replace----

a, b = sys.stdin.readline().split()
print(int(a.replace('6','5')) + int(b.replace('6','5')), int(a.replace('5','6')) + int(b.replace('5','6')))