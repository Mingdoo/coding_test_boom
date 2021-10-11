def solution(prices):
    answer = []
    idx = 0
    N = len(prices)
    while idx < N:
        s = 0
        temp = prices[idx]
        for i in range(idx+1, N):
            if prices[i] < temp:
                answer.append(i-idx)
                s = 1
                break
        if s == 0:
            answer.append(N-idx-1)
        idx += 1

    return answer

print(solution([1, 2, 3, 2, 3]))