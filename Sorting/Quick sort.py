def quickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0] 

    less, equal, big = [], [], []
    for i in range(len(lst)):
        if lst[i] > pivot: big.append(lst[i])
        elif lst[i] < pivot: less.append(lst[i])
        else: equal.append(lst[i])

    return quickSort(less) + equal + quickSort(big)

if __name__ == "__main__":
    lst = [1,5,2,6,3,4]
    print(quickSort(lst))