lst_1 = [1, 2, 3, 4, 5] * 8
lst_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5
lst_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4


def solution(answers):
    result_1 = 0
    result_2 = 0
    result_3 = 0
    for i in range(len(answers)):
        temp = i % 40
        if answers[i] == lst_1[temp]:
            result_1 += 1
        if answers[i] == lst_2[temp]:
            result_2 += 1
        if answers[i] == lst_3[temp]:
            result_3 += 1
    answer = []
    scores = [result_1, result_2, result_3]
    winning_score = max(scores)
    for j in range(3):
        if scores[j] == winning_score:
            answer.append(j + 1)

    return answer

