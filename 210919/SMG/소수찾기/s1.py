from itertools import permutations
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    numbers_list = []
    for i in range(1, len(numbers)+1):
        numbers_list.append(set(map(''.join, permutations(numbers, i))))
    for i in numbers_list:
        for j in i:
            if int(j) >= 2 and j[0] != '0':
                if is_prime_num(int(j)):
                    answer += 1
    print(numbers_list)
    return answer

print(solution("011"))