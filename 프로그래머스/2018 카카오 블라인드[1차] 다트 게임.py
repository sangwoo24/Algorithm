import re
import math

def solution(score):
    index = -1
    dart = [0 for i in range(3)]
    bonus = {"S":1,"D":2,"T":3}
    option = {"*":2,"#":-1}
    
    s = ""
    for i in range(len(score)):
        if score[i] not in bonus and score[i] not in option:
            s += score[i]

        if score[i] in bonus:
            index += 1
            dart[index] = int(math.pow(int(s),bonus[score[i]]))
            s = ""
            
        if score[i] in option:
            if index != 0:
                if score[i] == "#":
                    dart[index] *= option[score[i]]
                else:
                    dart[index-1] *= option[score[i]]
                    dart[index] *= option[score[i]]
            else:
                dart[index] *= option[score[i]]
    return sum(dart)