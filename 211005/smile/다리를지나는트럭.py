def solution(bridge_length, weight, truck_weights):
    queue = []
    idx = 1
    temp = 0
    a = truck_weights.pop(0)
    queue.append((a, 1))
    temp += a
    while queue:
        if truck_weights:
            a = truck_weights.pop(0)
        else:
            a = 0

        if idx - queue[0][1] >= bridge_length:  # 시간지나서 나올 트럭있는지 확인
            x, y = queue.pop(0)
            temp -= x

        if temp + a > weight:  # 중량 초과하면 중량 괜찮을 때까지 내보내기
            while temp + a > weight:
                idx += 1
                if idx - queue[0][1] >= bridge_length:
                    x, y = queue.pop(0)
                    temp -= x

        if len(queue) + 1 > bridge_length:  # 들어갈 자리가 없다면 1개 내보내기
            while len(queue) + 1 > bridge_length:
                idx += 1
                if idx - queue[0][1] >= bridge_length:
                    x, y = queue.pop(0)
                    temp -= x

        if a != 0:
            queue.append((a, idx))
        temp += a
        idx += 1

    return idx - 1