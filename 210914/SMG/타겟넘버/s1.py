def solution(numbers, target):
    answer = 0
    def dfs(num, level):
        nonlocal answer
        if level == len(numbers):
            if num == target:
                answer += 1
            return
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))