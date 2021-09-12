import heapq

def solution(scoville, K):
    answer = []
    for element in scoville:
        heapq.heappush(answer, element)
    cnt = 0
    while answer[0] < K and len(answer) > 1:
        v1 = heapq.heappop(answer)
        v2 = heapq.heappop(answer)
        heapq.heappush(answer, v1 + 2 * v2)
        cnt += 1
    if answer[0] < K:
        return -1

    return cnt

print(solution([1,2,3,9,10,12], 7))