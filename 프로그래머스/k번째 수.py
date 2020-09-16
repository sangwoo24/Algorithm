'''

        array	                     commands	             return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
'''

def solution(array, commands):
    answer = []
    for i in range(3):
        lst = array[commands[i][0] - 1 : commands[i][1]]
        answer.append(sorted(lst)[commands[i][2] - 1])
    return answer


print(solution())