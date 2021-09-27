def solution(name):
    answer = 0
    for char in name:
        answer += min(abs(ord(char) - ord('A')), abs(ord(char) - ord('Z') - 1))
    # tmp1, tmp2 = 0, 0
    # first_idx = 0
    # if name[-1] == 'A':
    #     for i in range(-2, -len(name), -1):
    #         print(i)
    #         if name[i] == 'A':
    #             continue
    #         else:
    #             first_idx = abs(i+1)
    #             break
    #     print(first_idx)

    else:
        answer += len(name) - 1
    return answer

print(solution("ZZAAA"))
