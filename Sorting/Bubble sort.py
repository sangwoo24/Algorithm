def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


if __name__ == "__main__":
    lst = [5,3,2,1,6,4]
    print(bubbleSort(lst))