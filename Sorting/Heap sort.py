def heapify(unsorted, index, heap_size):
    largest = index
    # 0번부터 시작하는 List
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heapSort(lst):
    for i in range(len(lst) // 2 - 1, -1, -1):
        heapify(lst,i,len(lst))
    print("최대 heap 구성",lst)
    
    for i in range(len(lst) - 1, 0 , -1):
        lst[0], lst[i] = lst[i], lst[0]
        print("전 : ",lst)
        heapify(lst,0,i)
        print("후 : ",lst)

if __name__ == "__main__":
    lst = [5,2,4,6,1,3]
    heapSort(lst)