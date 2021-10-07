def solution(number, k):
    answer = []
    length = len(number)
    lst = list(number)
    curr = 0
    while length - curr > k:
        state = 1
        max_value = number[curr]
        max_idx = curr
        for i in range(curr, curr + k + 1):
            if number[i] == '9':
                answer.append('9')
                k -= i - curr
                curr = i + 1
                state = 0
                break
            if max_value < number[i]:
                max_value = number[i]
                max_idx = i

        if state:
            answer.append(max_value)
            k -= max_idx - curr
            curr = max_idx + 1

        if k == 0:
            answer += number[curr:]
            break

    return ''.join(answer)

print(solution("4177252841", 4))

