import sys
sys.stdin = open('input.txt')

T = int(input())


def find_road(i, j, l, K):
    dx = [0, 1, 0, -1]  # 상하좌우
    dy = [1, 0, -1, 0]
    visited[i][j] = l

    for n in range(4):
        x = i + dx[n]
        y = j + dy[n]
        if x in range(N) and y in range(N) and visited[x][y] == 0:
            if map_info[x][y] < map_info[i][j]:
                find_road(x, y, l+1, K)
            # elif map_info[x][y] == map_info[i][j] and K != 0:
            #     map_info[x][y] -= 1
            #     find_road(x, y, l+1, 0)
            #     map_info[x][y] += 1
            elif map_info[x][y] >= map_info[i][j] and K != 0:
                temp = map_info[x][y] - map_info[i][j]
                if temp+1 <= K:
                    map_info[x][y] -= (temp+1)
                    find_road(x, y, l+1, 0)
                    map_info[x][y] += (temp+1)

    answer.append(l)
    visited[i][j] = 0


for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N 한변의 길이, K 최대 공사 가능 깊이
    max_num = 0
    map_info = []
    answer = []
    visited = [[0] * N for _ in range(N)]
    status = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        if max(temp) > max_num:
            max_num = max(temp)
        map_info.append(temp)

    for i in range(N):
        for j in range(N):
            if map_info[i][j] == max_num:
                find_road(i, j, 1, K)
    print('#{} {}'.format(tc, max(answer)))