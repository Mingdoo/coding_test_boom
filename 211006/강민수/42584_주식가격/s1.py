def solution(prices):
    time = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                time[i] += 1
            else:
                time[i] += 1
                break
    return time

print(solution([1,2,3,2,3]))