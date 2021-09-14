import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        answer += 1
        if len(scoville) >= 3:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            temp = 2 * y + x
            if temp >= K and scoville[0] >= K:
                return answer
            heapq.heappush(scoville, temp)

        elif len(scoville) == 2:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            temp = 2 * y + x
            if temp >= K:
                return answer
            else:
                return -1





scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))