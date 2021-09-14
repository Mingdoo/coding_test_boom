def dp(n, num, a):
    b = 0
    for i in range(a-1, -1, -1):
        b += 10**i * n

    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif


def solution(N, number):
    a = len(str(number))
    answer = dp(N, number, a)
    return answer


print(solution(5, 12))