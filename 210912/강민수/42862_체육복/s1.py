def solution(n, lost, reserve):
    answer = 0
    people = [0 for _ in range(n+2)]
    for idx in lost:
        people[idx] -= 1
    for idx in reserve:
        people[idx] += 1

    for i in range(1, n+1):
        if people[i] == -1:
            if people[i-1] == 1:
                people[i] += 1
                people[i-1] -= 1
            elif people[i+1] == 1:
                people[i] += 1
                people[i+1] -= 1
    for j in range(1, n+1):
        if people[j] >= 0:
            answer += 1
    return answer

n = 5
lost = []
reserve = []
print(solution(n, lost, reserve))

n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))