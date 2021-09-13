maximum = 8
ans = 0
import math

def solution(N, number):
    dp_table = [set() for _ in range(9)]

    for it in range(1, 9):
        dp_table[it].add(int(str(N) * it))

    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp_table[j]:
                for num2 in dp_table[i-j]:
                    dp_table[i].add(num1 + num2)
                    dp_table[i].add(num1 - num2)
                    dp_table[i].add(num1 * num2)
                    if num2 != 0 and math.isclose(num1 / num2, int(num1 / num2)):
                        dp_table[i].add(num1 // num2)
        if number in dp_table[i]:
            return i
    return -1

print(solution(5,12))