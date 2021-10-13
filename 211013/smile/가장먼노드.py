def dfs(s):
    global graph, visited
    queue = [s]
    answer = 0

    while queue:
        s = queue.pop(0)
        for i in graph[s]:
            if visited[i] == 0:
                visited[i] = visited[s] + 1
                answer = visited[i]
                queue.append(i)

    return visited.count(answer)


def solution(n, edge):
    global graph, visited
    graph = [[] * (n+1) for _ in range(n+1)]
    visited = [0] * (n + 1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    visited[1] = 1
    answer = dfs(1)

    return answer



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))