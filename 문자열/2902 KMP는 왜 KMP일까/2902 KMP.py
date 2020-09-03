import sys

s = sys.stdin.readline().split('-')

for i in range(len(s)):
    s[i] = s[i][0]
    print(s[i],end = '')

# sys.stdin.readline().split('문자열')
# 문자열 기준으로 split -> list
# print 줄바꿈 제거 end = '원하는 문자열'
# 원하는 문자열이 줄바꿈 대신 들어감
