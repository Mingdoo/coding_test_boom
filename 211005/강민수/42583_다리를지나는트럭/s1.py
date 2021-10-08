from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque([0] * bridge_length)
    time = 0
    total = 0
    while truck:
        time += 1
        tr = truck.popleft()
        total -= tr
        if truck_weights:
            if total + truck_weights[0] <= weight:
                tr = truck_weights.pop(0)
                total += tr
                truck.append(tr)
            else:
                truck.append(0)
        else:
            return time + len(truck)

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))