import sys

st = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())

ans = []

for i in range(len(st)):
    ans.append(st[i])
    if len(ans) >= len(bomb):                    # 폭탄길이 이상으로 append됐을 때
        if ans[-len(bomb):] == bomb:             # 마지막 index부터 비교해서 폭탄과 같다면
            del ans[-len(bomb):]                 # 폭탄 길이만큼 삭제

print(''.join(ans) if len(ans) > 0 else "FRULA") # 삼항연산자 

'''
st = sys.stdin.readline().strip()
a = sys.stdin.readline().strip()
i = 0

while i <= (len(st)-len(a)):
    new = st[i:i+len(a)]
    if new == a:
        st = st.replace(new,"",1)
        i = 0
    else:
        i += 1
        
if st != "":
    print(st)
else:
    print("FRULA")
'''