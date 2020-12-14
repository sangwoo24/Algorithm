def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    merged_lst =[]
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged_lst.append(left[0])
            left = left[1:]
        else:
            merged_lst.append(right[0])
            right = right[1:]
    merged_lst += left
    merged_lst += right
    return merged_lst

if __name__ == "__main__":
    lst = [12,25,31,22,26]
    print(mergeSort(lst))
