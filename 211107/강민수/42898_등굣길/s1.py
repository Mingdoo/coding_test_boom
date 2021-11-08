def solution(m, n, puddles):
    board = [[0] * (m+1) for _ in range(n+1)]

    board[1][1] = 1
    # i는 row
    for i in range(1, n + 1):
        # j는 col
        for j in range(1, m + 1):
            if (i, j) == (1, 1):
                pass
            elif [j, i] in puddles:
                board[i][j] = 0
            else:
                board[i][j] = (board[i][j-1] + board[i-1][j]) % 1000000007

    return board[n][m]

print(solution(4,3,[[2,2]]))