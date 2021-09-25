def solution(name):
    answer = 0
    cnt = 0
    N = len(name)
    abc_lst = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    visited = [0] * N

    for i in range(N):
        if name[i] == 'A':
            visited[i] = 1

    n = 1
    while sum(visited) < N:
        if visited[cnt] == 0:
            a = abc_lst.index(name[cnt])
            if a > 13:  # 반이상 가야되면 뒤로가기
                a = abc_lst[::-1].index(name[cnt]) + 1
            visited[cnt] = 1
            answer += a

        if n == 1 and cnt + n in range(N) and visited[cnt + n] != 0:
            b = visited[::-1].index(0) + 1 + cnt
            if visited.index(0) - cnt >= b:  # 뒤로가는게 더 빠른지 확인
                n = -1
                cnt -= (b - 1)
                answer += (b - 1)

        answer += 1
        cnt += n

    return answer - 1


print('solution0', solution('JEROAAAEN'))
print('solution', solution('JEAAAROEN'))
print('solution2', solution("JAAAAAAAN"))
print(solution("AABBBBBBBBAAAAAAAAAABBBBBBBBBBBBBBAAAAAAAAAAD"), 7)