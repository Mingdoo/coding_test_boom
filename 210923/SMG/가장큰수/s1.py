from itertools import permutations


def solution(numbers):
    str_numbers = []
    for i in numbers:
        str_numbers.append(str(i))
    numbers_list = list(map(''.join, permutations(str_numbers)))
    max_result = int(numbers_list[0])
    for i in range(len(numbers_list)):
        if int(numbers_list[i]) > max_result:
            max_result = int(numbers_list[i])
    answer = str(max_result)
    return answer

print(solution([3, 30, 34, 5, 9]))