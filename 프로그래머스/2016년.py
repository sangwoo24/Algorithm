
def solution(a,b):
    month = dict()
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    for i in range(1,13):
        if i == 2:
            month[i] = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            month[i] = 30
        else:
            month[i] = 31
    day = 0
    for i in range(1,a):
        day += month[i]
    day += b - 1
    return days[day % 7]

print(solution(7,17))

