import copy

def solution(N, number):
    answer = 0

    arr = [set() for i in range(9)]


    for i in range(1,9):
        arr[i].add(int(str(N)*i))

    for i in range(1,9):
        for j in range(1,i):
            for item1 in arr[j]:
                for item2 in arr[i-j]:
                    arr[i].add(item1 + item2)
                    arr[i].add(item1 - item2)
                    arr[i].add(item1 * item2)
                    if item2 != 0:
                        arr[i].add(item1 // item2)

            if (number in arr[i]):
                return i

    return -1

print(solution(5,12))