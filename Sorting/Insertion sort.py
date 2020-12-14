def InsertionSort(lst):
    for i in range(1,len(lst)):
        j = i - 1
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j+1] = key
    print(lst)

def InsertionSort2(lst):
    for i in range(1,len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j], lst[j-1] = lst[j-1], lst[j]

if __name__ == "__main__":
    lst = [5,3,2,1,6,4]
    InsertionSort2(lst)