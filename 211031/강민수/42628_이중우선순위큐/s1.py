import heapq

def solution(operations):
    heap = []
    idx = -1
    for operation in operations:
        if operation.startswith('I'):
            heapq.heappush(heap, -int(operation[2:]))
        elif operation == 'D 1':
            if heap:
                heap.remove(min(heap))

        elif operation == 'D -1':
            if heap:
                heap.remove(max(heap))

    if len(heap) == 0:
        return [0, 0]
    else:
        print(heap)
        return [-min(heap), -max(heap)]

print(solution(["I 16","D 1"]))