def solution(priorities, location):

    answer = 0
    idx = 0
    n = len(priorities)

    while priorities:
        max_num = max(priorities)
        if priorities[idx % n] == max_num:
            priorities[idx % n] = 0
            answer += 1
            if idx % n == location:
                return answer
        idx += 1


def solution2(priorities, location):

    queue = list(range(len(priorities)))
    answer = 0
    while priorities:
        pri = max(priorities)
        temp1 = priorities.pop(0)
        temp2 = queue.pop(0)
        if pri != temp1:
            priorities.append(temp1)
            queue.append(temp2)
        else:
            answer += 1
            if temp2 == location:
                return answer

print(solution([2, 1, 3, 2], 1))
print(solution([1, 1, 9, 1, 1, 1], 0))