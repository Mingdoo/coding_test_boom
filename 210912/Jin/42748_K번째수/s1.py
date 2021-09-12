def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] - 1
        end = i[1]
        try:
            answer.append(sorted(array[start:end])[i[2] - 1])
        except:
            answer.append(sorted(array[start:])[i[2] - 1])
    return answer