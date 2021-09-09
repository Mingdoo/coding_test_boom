import sys

N, M = map(int, sys.stdin.readline().split())
titles = [0] * (N + 1)
values = [-1] + [0] * N + [10 ** 9 + 1]
for i in range(1, N + 1):
    temp1, temp2 = sys.stdin.readline().split()
    titles[i], values[i] = temp1, int(temp2)

for j in range(M):
    value = int(sys.stdin.readline())
    start = 1
    end = N

    while start <= end:
        mid = (start + end) // 2
        if value <= values[mid - 1]:
            end = mid - 1
        elif value > values[mid + 1]:
            start = mid + 2

        elif values[mid - 1] < value <= values[mid]:
            print(titles[mid])
            break

        elif values[mid] < value <= values[mid + 1]:
            print(titles[mid + 1])
            break