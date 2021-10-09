from collections import deque

def solution(prices):
    length = len(prices)
    answer = [0] * length
    stack = deque([0])
    for i in range(1, length):
        if prices[i] >= prices[stack[-1]]:
            stack.append(i)
        else:
            while stack and prices[stack[-1]] > prices[i]:
                temp = stack.pop()
                answer[temp] = i - temp
            stack.append(i)
    if stack:
        for i in stack:
            answer[i] = length - i - 1
    return answer