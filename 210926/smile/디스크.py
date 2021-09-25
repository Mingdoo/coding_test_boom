import heapq

def solution(jobs):
    answer = 0
    temp = -1
    idx = 0
    heap = []
    jobs.sort()
    current = 0

    while idx < len(jobs):
        for i in jobs:
            if i[0] in range(temp+1, current+1):  # 이전에 이미 계산한 건 제외해야됨 temp 설정
                heapq.heappush(heap, (i[1], i[0]))  # 요청시간 기준 힙 (무엇을 우선순위로 둘 것인가)
        temp = current
        if len(heap) > 0:  # 힙에 들어온 거 중에 가장 우선순위 빠른거 먼저 1개 하기
            x, y = heapq.heappop(heap)  # x 걸린시간 y 요청시간
            current += x
            answer += (current - y)
            idx += 1  # 종료조건
        else:  # 요청한 걸 다했는데 처리안한게 있는 경우를 위해
            current += 1

    return answer // len(jobs)


print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)