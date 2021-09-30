import sys
sys.stdin = open('sample_input.txt')

def find_highest_index(board):
    maximum = max([max(row) for row in board])
    res = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == maximum:
                res.append([i,j])
    return res

def find_route(board, r, c):
    N = len(board)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    res = []
    for i in range(4):
        if 0 <= r + dr[i] < N and 0 <= c + dc[i] < N:
            res.append([r + dr[i], c + dc[i]])
    return res

def dfs(point, board, bool):

    global answer
    if visited[point[0]][point[1]] > answer:
        answer = visited[point[0]][point[1]]

    for route in find_route(board, point[0], point[1]):
        if board[route[0]][route[1]] < board[point[0]][point[1]] and visited[route[0]][route[1]] == 0:
            visited[route[0]][route[1]] = visited[point[0]][point[1]] + 1
            dfs(route, board, bool)
            visited[route[0]][route[1]] = 0
        elif bool == 1 and board[route[0]][route[1]] - K < board[point[0]][point[1]] and visited[route[0]][route[1]] == 0:
            tmp = board[route[0]][route[1]]
            board[route[0]][route[1]] = board[point[0]][point[1]] - 1
            visited[route[0]][route[1]] = visited[point[0]][point[1]] + 1
            dfs(route, board, bool - 1)

            #초기화
            visited[route[0]][route[1]] = 0
            board[route[0]][route[1]] = tmp
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    start_points = find_highest_index(board)
    visited = [[0] * len(board) for _ in range(len(board))]
    answer = 0
    for point in start_points:
        visited[point[0]][point[1]] = 1
        dfs(point, board, 1)
        visited[point[0]][point[1]] = 0

    print(f'#{tc} {answer}')

