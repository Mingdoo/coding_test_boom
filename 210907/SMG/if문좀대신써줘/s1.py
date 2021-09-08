import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
level = [list(sys.stdin.readline().split()) for _ in range(N)]

for i in range(len(level)):
    level[i][1] = int(level[i][1])

power = [int(sys.stdin.readline()) for _ in range(M)]

for i in range(len(power)):
    for j in range(len(level)):
        if j == 0:
            if power[i] <= level[j][1]:
                print(level[j][0])
        elif level[j-1][1] < power[i] <= level[j][1]:
            print(level[j][0])
