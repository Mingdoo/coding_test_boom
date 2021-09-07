import sys
sys.stdin = open('input.txt')

T = int(input())


def binary_search(start, end, i):

    while start != end:
        mid = (start + end) // 2
        if lst[mid][1] >= i:
            end = mid
        else:
            start = mid
    return lst[start][0]


for tc in range(1, T+1):
    N, M = map(int, input().split())  # N 칭호개수, M 캐릭터 개수
    lst = []
    for _ in range(N):
        n, n_range = input().split()
        lst. append([n, int(n_range)])
    arr = [int(input()) for _ in range(M)]

    for i in arr:
        print(binary_search(0, N-1, i))
