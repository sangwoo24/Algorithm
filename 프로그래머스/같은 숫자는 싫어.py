

lst = [1,1,3,3,0,1,1]
#[1,-1,3]

m = lst[0]
for i in range(1,len(lst)):
    if m == lst[i]:
        m = lst[i]
        lst[i] = -1
    else:
        m = lst[i]
    
print([i for i in lst if i != -1])