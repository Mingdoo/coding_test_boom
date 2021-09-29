from collections import deque
import heapq

def solution(jobs):
    curr = 0
    length = len(jobs)
    sorted_lst = sorted(jobs, key=lambda x: x[0])
    dq = deque(sorted_lst)
    heap = []
    times = []
    while dq:
        while dq and dq[0][0] <= curr:
            temp = dq.popleft()
            heapq.heappush(heap, (temp[1], temp))
        if heap:
            pri = heapq.heappop(heap)
            curr += pri[1][1]
            times.append(curr - pri[1][0])
        else:
            temp = dq.popleft()
            heapq.heappush(heap, (temp[1], temp))
            curr = temp[0]
            continue

    while heap:
        primary = heapq.heappop(heap)
        curr += pri[1][1]
        times.append(curr - primary[1][0])

    answer = sum(times) // length
    return answer