import itertools

# 에라토스테네스의 체
prime_numbers = [0, 0] + [1] * (10000000 - 2)
for i in range(2, 10000):
    if prime_numbers[i]:
        for j in range(2, 10000000 // i):
            prime_numbers[j * i] = 0
    else:
        for j in range(2, 10000000 // i):
            prime_numbers[j * i] = 0


def solution(numbers):
    length = len(numbers)
    answer = 0
    temp_set = []
    for i in range(1, length + 1):
        p = itertools.permutations(list(numbers), i)
        for j in p:
            target = int(''.join(list(j)))
            if prime_numbers[target] and target not in temp_set:
                temp_set.append(target)
                answer += 1

    return answer