def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]
    while priorities:
        a = priorities.pop(0)
        b = idx.pop(0)
        if priorities and a < max(priorities):
            priorities.append(a)
            idx.append(b)
        else:
            if b == location:
                answer += 1
                return answer
            else:
                answer += 1
    return answer