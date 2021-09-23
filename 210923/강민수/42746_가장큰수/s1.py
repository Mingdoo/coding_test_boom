def solution(numbers):
    numbers = sorted(map(str, numbers), reverse=True, key=lambda x: str(x)*3)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))