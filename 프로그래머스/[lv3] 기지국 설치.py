import math

def solution(apt, stations, band):
    fill = []
    ans = 0
    start = 1
    for i in range(len(stations)):
        fill.append(stations[i] - band - start)
        start = stations[i] + band + 1 
    fill.append((apt+1) - start)
    
    for i in range(len(fill)):
        if fill[i] > 0:
            ans += math.ceil(fill[i] / (band*2+1))
    return ans