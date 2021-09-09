def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progress = progresses.pop(0)
            speed = speeds.pop(0)
            progresses.append(progress + speed)
            speeds.append(speed)
        idx = 0
        for j in range(len(progresses)):
            if progresses[j] >= 100:
                idx += 1
            else:
                break
        if idx >= 1:
            answer.append(idx)
        progresses = progresses[idx:]
        speeds = speeds[idx:]
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
