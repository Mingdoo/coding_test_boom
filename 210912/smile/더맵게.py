import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + (s2 * 2))
        answer += 1
    if max(scoville) < K:
        return -1

    return answer

def solution2(scoville, K):
    scoville.sort()




scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))


