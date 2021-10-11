def solution(n, computers):
    global network
    network = [-1] * n

    for i in range(n):
        dfs(i, i, n, computers)

    return len(set(network))


def dfs(j, a, n, computers):
    global network

    state = 0
    for k in range(n):
        if network[k] == -1 and computers[j][k] == 1:
            state = 1
            network[k] = a
            dfs(k, a, n, computers)

    if state == 0:
        if network[a] == -1:
            network[a] = a

    return


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))

print(solution(5, [[1, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1]]	))

