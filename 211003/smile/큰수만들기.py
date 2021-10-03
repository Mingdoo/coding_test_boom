def solution(number, k):
    answer = ''
    while k:
        if len(number) == k:
            number = ''
            break
        if '9' in number[:k+1]:
            temp = '9'
        else:
            temp = max(number[:k+1])
        i = number.find(temp)
        answer += number[i]
        number = number[i + 1:]
        k -= i
    answer += number

    return answer


print(solution("1924", 2))  #94
print(solution("1231234", 3))  # 3234
print(solution("4177252841", 4))  #775841
print(solution("9999999", 6))
print(solution("1234565", 6))
print(solution("1111", 2))
print(solution("9811", 2))