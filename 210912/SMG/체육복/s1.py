def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n + 1)
    for i in lost:
        students[i] -= 1
    for i in reserve:
        students[i] += 1

    for i in range(1, len(students)):
        if i == (len(students)-1):
            if students[i] == 0:
                if students[i - 1] == 2:
                    students[i] += 1
                    students[i - 1] -= 1
        elif students[i] == 0:
            if students[i - 1] == 2:
                students[i] += 1
                students[i - 1] -= 1
            elif students[i + 1] == 2:
                students[i] += 1
                students[i + 1] -= 1

    answer = len(students) - students.count(0) - 1

    return answer

print(solution(3, [3], [1]))