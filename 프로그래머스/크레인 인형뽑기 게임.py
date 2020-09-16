def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i - 1] != 0:
                stack.append(j[i - 1])
                j[i - 1] = 0
                if len(stack) >= 2:
                    if stack[len(stack) - 1] == stack[len(stack) - 2]:
                        answer += 2
                        stack.pop()
                        stack.pop()
                break
    return answer
'''
def solution(board, moves):
    stack = []
    answer = 0
    for move_index in moves:
        for board_index in range(len(board)):
            if board[board_index][move_index - 1] != 0:  
                stack_input_data = board[board_index][move_index - 1]        
                if len(stack) == 0:
                    stack.append(stack_input_data)
                    board[board_index][move_index - 1] = 0
                    break
                else:
                    if stack_input_data == stack[len(stack) - 1]:
                        stack.pop()
                        board[board_index][move_index - 1] = 0
                        answer += 2
                    else:
                        stack.append(stack_input_data)
                        board[board_index][move_index - 1] = 0
                    break 
    return answer
'''

if __name__ == "__main__":
    
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    #print(solution(board,moves))
    