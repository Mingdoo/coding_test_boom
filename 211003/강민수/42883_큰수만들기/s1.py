def solution(number, k):
    checked = ''
    tmp = -1
    for i in range(len(number) - k):
        maximum = ''
        for j in range(tmp + 1, len(number)):
            if (len(number) - k - len(checked)) <= len(number) - j:
                if number[j] == '9':
                    maximum = number[j]
                    tmp = j
                    break
                elif number[j] > maximum:
                    maximum = number[j]
                    tmp = j
            else:
                break
        checked += maximum
    return checked

print(solution('4177252841', 4))