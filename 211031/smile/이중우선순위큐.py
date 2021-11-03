import heapq

def solution(operations):
    cnt = 0

    for o in operations:
        if cnt == 0:
            heap1 = []
            heap2 = []

        if o[0] == 'I':
            num = int(o[2:])
            heapq.heappush(heap1, -num)
            heapq.heappush(heap2, num)
            cnt += 1
        elif o == 'D 1':  # 최댓값 삭제
            if heap1:
                heapq.heappop(heap1)
                cnt -= 1
        else:  # 최솟값 삭제
            if heap2:
                heapq.heappop(heap2)
                cnt -= 1

    if cnt > 0:
        a = heapq.heappop(heap1)
        b = heapq.heappop(heap2)
        answer = [-a, b]
    else:
        answer = [0, 0]

    return answer