def solution(answers):
    n = len(answers)
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    score = [0, 0, 0]
    max_score = 0

    for i in range(n):
        if answers[i] == s1[i%5]:
            score[0] += 1
        if answers[i] == s2[i%8]:
            score[1] += 1
        if answers[i] == s3[i%10]:
            score[2] += 1

    for idx, j in enumerate(score):
        if j > max_score:
            answer = [idx+1]
            max_score = j
        elif j == max_score:
            answer.append(idx+1)

    return answer



answers2 = [1,2,3,4,5]
answers = [1,3,2,4,2]
print(solution(answers))