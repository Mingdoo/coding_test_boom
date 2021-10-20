def dfs(s, result, path):
    global answer

    if answer:
        return

    if s not in path or len(path[s]) == 0:
        if len(result) == N + 1:
            answer = result
        return

    for i in range(len(path[s])):
        tmp = path[s].pop(i)
        dfs(tmp, result + [tmp], path)
        path[s].insert(i, tmp)


def solution(tickets):
    global answer, N
    N = len(tickets)
    answer = []
    path = {}

    for t in tickets:
        path[t[0]] = path.get(t[0], []) + [t[1]]
        path[t[0]].sort()

    dfs('ICN', ['ICN'], path)

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))