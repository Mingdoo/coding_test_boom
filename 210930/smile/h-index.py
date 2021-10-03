def solution(citations):
    citations.sort(reverse=True)  # 65310
    n = len(citations)

    for i in range(1, n+1):
        if citations[i-1] < i:
            return i-1
    return n


print(solution([0, 0, 5, 5, 5, 8, 8, 9, 10, 11, 12, 13, 14]))
print(solution([3, 0, 6, 1, 5]))
print(solution([1, 1, 1, 1]))
print(solution([0, 22, 42]))
print(solution([22, 42]))  # 9번 테스트케이스