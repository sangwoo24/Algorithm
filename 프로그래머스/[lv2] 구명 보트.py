def solution(people, limit):
    people = sorted(people)
    cnt = 0
    min_index, max_index = 0,len(people) - 1
    
    while min_index <= max_index:
        cnt += 1
        if people[min_index] + people[max_index] <= limit:
            min_index += 1
        max_index -= 1
    return(cnt)
# 정렬 후, 가장 최적의 효과를 내기 위해 제일 작은 무게의 사람과 제일 큰 무게의 사람을 더한게 제한에
# 안걸리면, 둘다 태워 보내고, 제한이 넘는다면 제일 큰 사람만 보낸다(그리디 알고리즘)
