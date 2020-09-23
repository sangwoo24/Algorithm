def solution(skill, skill_trees):
    cnt = 0
    
    for i in range(len(skill_trees)):
        index = 0
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                if skill_trees[i][j] == skill[index]:
                    index += 1
                else:
                    cnt += 1
                    break
    return len(skill_trees) - cnt