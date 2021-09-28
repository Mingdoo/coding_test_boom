def solution(name):
    answer = [min(abs(ord(char) - ord('A')), abs(ord(char) - ord('Z') - 1)) for char in name]
    left_to_right = 1000000
    print(answer)
    longest = 0
    for i in range(len(name)):
        tmp = 0
        if name[i] == 'A':
            tmp += 1
            for j in range(i+1, len(name)):
                if name[j] == 'A':
                    tmp += 1
                else:
                    break
            if tmp > longest:
                longest = tmp
    if name[-1] == 'A':
        left_to_right = sum(answer)
        cnt = 1
        for i in range(len(name)-2, -1, -1):
            if name[i] == 'A':
                cnt += 1
            else:
                break
        left_to_right += len(name) - cnt - 1
    brute_force = sum(answer) + len(name) - 1
    greedy = 0
    idx = 0
    direction = 1
    visited = [0] * len(name)
    while True:
        greedy += answer[idx]
        answer[idx] = 0
        visited[idx] = 1

        if idx == len(name) - 1 and direction == 1:
            break

        if visited[idx + direction] == 1:
            break
        temp = 0
        if direction == 1 and name[idx + direction] == 'A':
            temp += 1
            kk = idx + direction
            for i in range(idx+direction+1, len(name)):
                if name[i] == 'A':
                    temp += 1
                    kk = i
                else:
                    break
            if temp >= longest:
                for ll in range(idx+direction, kk+1):
                    visited[ll] = 1
                greedy += idx + 1
                idx = -1
                direction = -1
                continue
            else:
                direction = 1
        greedy += 1
        idx += direction

    return min(left_to_right, greedy, brute_force)