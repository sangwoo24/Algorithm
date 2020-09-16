def solution(arr, divisor):
    for i in range(len(arr)):
        if arr[i] % divisor != 0:
            arr[i] = -1
    if arr.count(-1) == len(arr):
        return [-1]
    else:
        return[i for i in arr if i != -1]
    



