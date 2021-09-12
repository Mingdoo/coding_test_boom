def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    d = [a, b, c]
    result = []
    for ans in d:
        total = 0
        for i in range(len(answers)):
            if answers[i] == ans[i]:
                total += 1
        result.append(total)

    for idx, i in enumerate(result):
        if i == max(result):
            answer.append(idx + 1)

    return answer

print(solution([1, 2, 3, 4, 5]))

