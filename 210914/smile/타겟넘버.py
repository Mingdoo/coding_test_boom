from itertools import combinations
# 319.13ms
def solution(numbers, target):
    answer = 0
    a = sum(numbers)

    if a == target:
        return 1
    else:
        b = a - target

    for i in range(1, len(numbers)):
        for j in list(combinations(numbers, i)):
            if sum(j) * 2 == b:
                answer += 1

    return answer

# 2382.96ms
def solution2(numbers, target):
    answer = 0
    a = sum(numbers)

    if a == target:
        return 1
    else:
        b = a - target

    n = len(numbers)
    for k in range(1, 1<<n):
        temp = []
        for l in range(n):
            if k & (1<<l):
                temp.append(numbers[l])
        if sum(temp) * 2 == b:
            answer += 1

    return answer



print(solution2([1, 1, 1, 1, 1], 3))