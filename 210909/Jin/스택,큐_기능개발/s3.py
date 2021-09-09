import math

def solution(progresses, speeds):
    length = len(progresses)
    days = []
    for i in range(length):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    answer = []
    temp = days[0]
    works = 1
    for j in range(1, length):
        if days[j] <= temp:
            works += 1
        else:
            answer.append(works)
            works = 1
            temp = days[j]
        if j == (length - 1):
            answer.append(works)
    return answer

pro1 = [93, 30, 55]
sp1 = [1, 30, 5]

pro2 = [95, 90, 99, 99, 80, 99]
sp2 = [1, 1, 1, 1, 1, 1]
print(solution(pro1, sp1))
print(solution(pro2, sp2))