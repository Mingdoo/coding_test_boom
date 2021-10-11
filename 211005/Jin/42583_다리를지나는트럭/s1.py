from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq = deque(truck_weights)
    curr = deque([0] * bridge_length)
    total = 0
    time = 0
    while dq:
        time += 1
        total -= curr.popleft()
        if total + dq[0] <= weight:
            temp = dq.popleft()
            curr.append(temp)
            total += temp
        else:
            curr.append(0)

    return time + bridge_length