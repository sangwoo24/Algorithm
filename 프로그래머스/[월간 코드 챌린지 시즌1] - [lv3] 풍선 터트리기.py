'''
import heapq
def solution(a):
    cnt = 0
    for i in range(len(a)):
        left,right = a[0:i],a[i+1:]        
        heapq.heapify(left)
        heapq.heapify(right)
        
        if not left or not right:
            cnt += 1
        else:
            if a[i] <= left[0] or a[i] <= right[0]:
                cnt += 1
    return (cnt)
    '''
    # --> 시간복잡도 O(N^2)이라 시간초과(heapq.heapify)

import math

def solution(a):
    cnt = 0
    left_arr = [(-math.inf)] * len(a)
    right_arr = [(-math.inf)] * len(a)
    
    left_value = math.inf
    right_value = math.inf
    for i in range(len(a)):
        if a[i] <= left_value:
            left_arr[i] = a[i]
            left_value = a[i]
        else:
            left_arr[i] = left_value
            
    for i in range(len(a)-1, -1, -1):
        if a[i] <= right_value:
            right_arr[i] = a[i]
            right_value = a[i]
        else:
            right_arr[i] = right_value
    
    for i in range(len(a)):
        if a[i] <= left_arr[i] or a[i] <= right_arr[i]:
            cnt += 1
    return cnt
    # --> 시간복잡도 O(N)으로 통과
    