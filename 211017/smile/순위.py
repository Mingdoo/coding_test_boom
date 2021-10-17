def solution(n, results):
    answer = 0
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    for r in results:
        win[r[0]].append(r[1])
        lose[r[1]].append(r[0])

    for i in range(1, n + 1):
        for j in win[i]:
            for k in lose[i]:
                if k not in lose[j]:
                    lose[j].append(k)

        for j in lose[i]:
            for k in win[i]:
                if k not in win[j]:
                    win[j].append(k)

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer