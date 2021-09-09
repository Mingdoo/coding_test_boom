import math

def solution(progresses, speeds):
    length = len(progresses)
    days = []
    for i in range(length):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    stack = [days[0]]
    answer = []
    for day in days[1:]:
        if stack:
            if stack[0] >= day:
                stack.append(day)
            else:
                answer.append(len(stack))
                stack = [day]
    if stack:
        answer.append(len(stack))

    return answer



pro1 = [93, 30, 55]
sp1 = [1, 30, 5]

pro2 = [95, 90, 99, 99, 80, 99]
sp2 = [1, 1, 1, 1, 1, 1]
print(solution(pro1, sp1))
print(solution(pro2, sp2))