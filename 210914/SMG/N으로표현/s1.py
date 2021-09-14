def solution(N, number):
    answer = 0
    case = [[] for _ in range(8)]
    case[0].append(N)

    for i in range(len(case)):
        for j in range(len(case[i])):
            case[i].append(case[i - 1][j] + N)
            case[i].append(case[i - 1][j] - N)
            case[i].append(case[i - 1][j] * N)
            case[i].append(case[i - 1][j] / N)
            case[i].append(int(str(case[i - 1][j]) + str(N) + str(N)))
            for num in case[i]:
                if num == number:
                    return i

    return answer

print(solution(5, 12))