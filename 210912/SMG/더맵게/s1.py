import heapq


def solution(scoville, K):
    answer = 0
    h = []
    for value in scoville:
        heapq.heappush(h, value)
    while h[0] <= K and len(h) >= 2:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        heapq.heappush(h, (a + (b*2)))
        answer += 1
    if max(h) < K:
        return -1
    return answer