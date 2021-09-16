def solution(priorities, location):
    idx = 0
    answer = 0
    length = len(priorities)
    highest = max(priorities)
    while True:
        if priorities[idx % length] and priorities[idx % length] == highest:
            if (idx % length) != location:
                priorities[idx % length] = 0
                answer += 1
                highest = max(priorities)
            else:
                answer += 1
                break
        idx += 1
    return answer