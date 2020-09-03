import sys

while True:
    flag = 0
    stack = []
    n = input()
    if n == ".":
        break

    for i in range(len(n)):
        if n[i] == "(" or n[i] == "[":
            stack.append(n[i])

        elif n[i] == ")":
            if len(stack) == 0:
                flag = 1
                break
            elif stack[-1] == "(":
                stack.pop()
            else:
                flag = 1
                break
            
        elif n[i] == "]":
            if len(stack) == 0:
                flag = 1
                break

            elif stack[-1] == "[":
                stack.pop()
            else:
                flag = 1
                break
    if flag == 1 or len(stack) != 0:
        print("no")
    else:
        print("yes")
            
    

            
