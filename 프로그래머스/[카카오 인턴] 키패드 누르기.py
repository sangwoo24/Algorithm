def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]
    phone = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2)]
    last_left = 10
    last_right = 11
    ans = []
    
    for i in range(len(numbers)):
        if numbers[i] in left:
            ans.append("L")
            last_left = numbers[i]
        elif numbers[i] in right:
            ans.append("R")
            last_right = numbers[i]
        else:#last값이 없을 수 있음.(한쪽만 없을수도), last부터 현재 번호까지 거리 구함, 같을 시 오른손 왼손으로 구분
            left_distance = abs(phone[last_left][0] - phone[numbers[i]][0]) + abs(phone[last_left][1] - phone[numbers[i]][1])
            right_distance = abs(phone[last_right][0] - phone[numbers[i]][0]) + abs(phone[last_right][1] - phone[numbers[i]][1])
            if left_distance == right_distance: # distance 같을 시
                if hand == "right":
                    ans.append("R")
                    last_right = numbers[i]
                else:
                    ans.append("L")
                    last_left = numbers[i]
            else: # distance 다를 시 
                if right_distance > left_distance: #왼쪽손가락 눌러야함(오른쪽이 더 큼)
                    ans.append("L")
                    last_left = numbers[i]
                else:
                    ans.append("R")
                    last_right = numbers[i]
    return ''.join(ans)