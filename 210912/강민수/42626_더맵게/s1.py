import heapq

def solution(scoville, K):
    heap = []
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])
    cnt = 0
    while heap[0] <= K:
        if len(heap) == 1:
            return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+2*b)
        cnt += 1
    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))