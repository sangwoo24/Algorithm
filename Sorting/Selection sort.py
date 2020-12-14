def selectionSort(lst):
    for i in range(len(lst)-1):
        mn_idx = i 
        for j in range(i+1,len(lst)):
            if lst[j] < lst[mn_idx]:
                mn_idx = j
        #if i != mn_idx:
        lst[i], lst[mn_idx] = lst[mn_idx], lst[i]
    return lst


if __name__ == "__main__":
    lst = [5,3,2,1,6,4]
    print(selectionSort(lst))