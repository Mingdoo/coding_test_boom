def solution(n, computers):
    answer = 0
    linked = [[] for _ in range(n)]
    visited = [0] * n
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                linked[i].append(j)

    stack = []
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            stack.append(i)
            while stack:
                v = stack.pop()
                for node in linked[v]:
                    if visited[node] == 0:
                        visited[node] = 1
                        stack.append(node)

    return answer

print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))