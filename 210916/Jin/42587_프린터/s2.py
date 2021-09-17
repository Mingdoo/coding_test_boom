# 가장 빠른 방법
def solution(priorities, location):
    idx = 0
    answer = 0
    length = len(priorities)
    sorted_lst = sorted(priorities, reverse=True)
    cnt = 0
    while True:
        if priorities[idx % length] and priorities[idx % length] == sorted_lst[cnt]:
            if (idx % length) != location:
                priorities[idx % length] = 0
                answer += 1
                cnt += 1
            else:
                answer += 1
                break
        idx += 1
    return answer