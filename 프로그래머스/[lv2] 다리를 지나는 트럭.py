def solution(bridge_length, weight, truck_weights):
    QUEUE = [0 for i in range(bridge_length)]
    time = 0
    index = 0

    while True:
        time += 1
        QUEUE.pop(0)
        if sum(QUEUE) + truck_weights[index] <= weight:
            QUEUE.append(truck_weights[index])
            index += 1
        else:
            QUEUE.append(0)
            
        if index >= len(truck_weights):
            break
    return len(QUEUE) + time