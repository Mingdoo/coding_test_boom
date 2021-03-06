def dfs(numbers, target, total, idx):
    global cnt

    if idx == len(numbers):
        if target == total:
            cnt += 1
        return

    dfs(numbers, target, total + numbers[idx], idx + 1)
    dfs(numbers, target, total - numbers[idx], idx + 1)

cnt = 0
def solution(numbers, target):
    global cnt
    #init block
    total = 0
    idx = 0

    dfs(numbers, target, total, idx)

    return cnt
