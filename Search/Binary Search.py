def binarySearch(lst, data):
    if len(lst) <= 1:
        if lst[0] != data:
            return None
        else:
            return True
    
    mid = (0 + len(lst)-1) // 2
    if data < lst[mid]:
        return binarySearch(lst[:mid],data)
    elif data == lst[mid]:
        return True
    elif data > lst[mid]:
        return binarySearch(lst[mid+1:],data)

if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7]
    print(binarySearch(lst,5))