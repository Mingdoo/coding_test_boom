import sys
sys.stdin = open('input.txt')


def binary_search(start, end, i):

    while start <= end:
        mid = (start + end) // 2
        if lst[mid][1] >= i:
            end = mid - 1
        else:
            start = mid + 1
    return lst[start][0]


N, M = map(int, input().split())  # N 칭호개수, M 캐릭터 개수
lst = []
for _ in range(N):
    n, n_range = input().split()
    lst. append([n, int(n_range)])

for _ in range(M):
    i = int(input())
    print(binary_search(0, N-1, i))