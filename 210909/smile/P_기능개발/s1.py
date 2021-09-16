def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    day_count = 1
    idx = 0

    while idx < N :
        a = progresses[idx]
        if a + day_count * speeds[idx] < 100:
            while a < 100:
                day_count += 1
                a = progresses[idx] + day_count * speeds[idx]
            cnt = 1
        else:
            cnt += 1
            if len(answer):
                answer.pop()
        answer.append(cnt)
        idx += 1
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
