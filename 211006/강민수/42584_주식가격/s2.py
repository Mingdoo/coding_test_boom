from collections import deque

def solution(prices):
    time = [0] * len(prices)
    prices = deque(prices)
    n = 0
    while prices:
        v = prices.popleft()
        cnt = 0
        for element in prices:
            if element >= v:
                cnt += 1
            else:
                cnt += 1
                break
        time[n] = cnt
        n += 1
    return time

print(solution([1,2,3,2,3]))