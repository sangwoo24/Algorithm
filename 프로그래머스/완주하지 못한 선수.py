#풀이 1
'''
def solution(participant, completion):
    answer = ''
    par = dict(zip(participant, [0] * len(participant)))
    com = dict(zip(completion,[0] * len(completion)))

    for name in participant:
        par[name] += 1
    for name in completion:
        com[name] += 1

    for name in par:
        try:
            if par[name] != com[name]:
                answer = name
                return answer
        except:
            answer = name
            return answer
'''


#풀이 2
'''
def solution(participant, completion):
    answer = ''
    par = dict()
    com = dict()
    
    for name in participant:
        if name in par:
            par[name] += 1
        else:
            par[name] = 0
            par[name] += 1

    for name in completion:
        if name in com:
            com[name] += 1
        else:
            com[name] = 0
            com[name] += 1

    for name in par:
        try:
            if par[name] != com[name]:
                answer = name
                return answer
        except:
            answer = name
            return answer
'''

#풀이 3
import collections
def solution(participant,completion):
    answer = list(collections.Counter(participant) - collections.Counter(completion))
    return answer[0]


#a = ['leo', 'kiki', 'eden','kiki'] #par
#b = ['eden', 'kiki'] #com

#a = ["marina", "josipa", "nikola", "vinko", "filipa"]
#b = ["josipa", "filipa", "marina", "nikola"]

a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]
print(solution(a,b))
