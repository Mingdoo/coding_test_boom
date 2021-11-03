def find_set(x):
    global p
    while x != p[x]:
        x = p[x]
    return x


def solution(n, costs):
    global p
    costs.sort(key = lambda x: x[2])
    p = [i for i in range(n)]
    cnt = 0
    total = 0
    for u, v, w in costs:
        if find_set(u) != find_set(v):
            cnt += 1
            total += w
            p[find_set(v)] = find_set(u)
            if cnt == n:
                break
    answer = total
    print(p)
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))