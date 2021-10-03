def solution(brown, yellow):

    S = brown + yellow
    answer = []

    for i in range(1, yellow+1):
        temp = yellow // i
        if i+2 >= temp+2 and (i+2)*(temp+2) == S and (i+2+temp)*2 == brown:
            answer = [i+2, temp+2]
            break

    return answer

print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]