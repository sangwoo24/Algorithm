import sys

st_suffix = []
st = list(sys.stdin.readline().strip())

for i in range(len(st)):
    if i >= 1:
        del st[0]
    st_suffix.append(''.join(st)) 
    
for i in sorted(st_suffix):
   print(i)    