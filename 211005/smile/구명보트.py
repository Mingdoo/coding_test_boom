def solution2(people, limit):
    answer = 0
    while people:
        a = people.pop(0)  # 인덱스
        for i in range(limit-a, 39, -1):
            if i in people:
                people.remove(i)
                break
        answer += 1

    return answer

def solution(people, limit):
    answer = 0
    people_dict = {}

    for i in people:
        people_dict[i] = people_dict.get(i, 0) + 1

    for i, k in people_dict.items():
        while k != 0:
            people_dict[i] -= 1
            for j in range(limit-i, 39, -1):
                if j in people_dict and people_dict[j] > 0:
                    people_dict[j] -= 1
                    break
            answer += 1
            k = people_dict[i]

    return answer


print(solution([70, 50, 80, 50], 100))