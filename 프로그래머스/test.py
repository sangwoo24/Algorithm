lst = [ [[100,1],[200,2],[300,3]],[[400,4]],[[500,5],[600,6]] ]

for i in range(3):
    n = 0
    while n < 2 and n < len(lst[i]):
        print(lst[i][n][0])
        n += 1