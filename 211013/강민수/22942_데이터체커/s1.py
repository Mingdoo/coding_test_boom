import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline
from collections import deque
N = int(input())

circles = [list(map(int, input().split())) for _ in range(N)]
circles = deque(sorted(circles, key=lambda a: a[0]+a[1]))

flag = True
while circles and flag:
    v = circles.pop()
    idx = -1
    while circles and abs(idx) <= len(circles) and circles[idx][0] + circles[idx][1] >= v[0] - v[1]:
        x = circles[idx][0]
        r = circles[idx][1]
        if x + r == v[0] + v[1]:
            flag = False
            break
        elif x - r == v[0] - v[1]:
            flag = False
            break
        elif abs(r - v[1]) < abs(x - v[0]) < r + v[1]:
            flag = False
            break
        elif abs(x - v[0]) == r + v[1]:
            flag = False
            break
        idx -= 1

if not flag:
    print('NO')
else:
    print('YES')