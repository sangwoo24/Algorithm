def solution(participant, completion):
    answer = ''
    par = dict(zip((participant),[0]*len(participant)))
    com = dict(zip((completion),[0]*len(completion)))
    #return answer
    for name in participant:
        par[name] += 1
    for name in completion:
        com[name] += 1


    for name in participant:
        if name not in com:
            print("ㅁ" ,name)
        else:
            if par[name] - com[name] != 0:
                print("ㅛ",name)


if __name__ == "__main__":
    a = ['석상우','전민주','김준혁','석상우']
    b = ['석상우','전민주']

    solution(a,b)