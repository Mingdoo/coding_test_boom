

def bfs(numbers, target, total, idx):
    global cnt

    if idx == len(numbers):
        if target == total:
            cnt += 1
        return

    bfs(numbers, target, total + numbers[idx], idx + 1)
    bfs(numbers, target, total - numbers[idx], idx + 1)

cnt = 0
def solution(numbers, target):
    global cnt
    total = 0
    idx = 0

    bfs(numbers, target, total, idx)

    return cnt
