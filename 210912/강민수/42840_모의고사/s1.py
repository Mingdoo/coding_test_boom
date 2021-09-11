def maximum(array):
    temp_max = array[0]
    for i in range(1, len(array)):
        if array[i] > temp_max:
            temp_max = array[i]
    return temp_max

def solution(answers):

    A = [1, 2, 3, 4, 5] * 2000
    B = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    A_count = 0
    B_count = 0
    C_count = 0
    for index in range(0, len(answers)):
        if (A[index] == answers[index]):
            A_count += 1

        if (B[index] == answers[index]):
            B_count += 1

        if (C[index] == answers[index]):
            C_count += 1

    counts = [A_count, B_count, C_count]

    result = []
    if A_count == maximum(counts):
        result.append(1)

    if B_count == maximum(counts):
        result.append(2)

    if C_count == max(counts):
        result.append(3)

    return result


answers = [1,2,3,4,5]
print(solution(answers))



