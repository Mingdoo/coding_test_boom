import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
grade = [sys.stdin.readline().split() for _ in range(N)]

def binary_search(grade, num):
    start, end = 0, len(grade) - 1
    while start <= end:
        mid = (start + end) // 2
        if num <= int(grade[mid][1]):
            end = mid - 1
        else:
            start = mid + 1
    return start
for _ in range(M):
    num = int(sys.stdin.readline())
    print(grade[binary_search(grade, num)][0])