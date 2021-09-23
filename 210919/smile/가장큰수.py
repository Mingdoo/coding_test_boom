# 정답
def solution(numbers):
    my_dict = {}
    answer = ''

    for i in numbers:
        i = str(i)
        n = 4 - len(i)

        if i + i[0]*n in my_dict:
            if my_dict.get(i + i[0]*n, '') + i > i + my_dict.get(i + i[0]*n, ''):
                my_dict[i + i[0]*n] = my_dict.get(i + i[0]*n, '') + i
            else:
                my_dict[i + i[0]*n] = i + my_dict.get(i + i[0]*n, '')
        else:
            my_dict[i + i[0]*n] = i

    sort_dict = sorted(my_dict, reverse=True)

    for num in sort_dict:
        answer += my_dict[num]

    return str(int(answer))

# 시간초과
def solution3(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    n = len(numbers)

    for i in range(n-1, 0, -1):
        if numbers[i-1]+numbers[i] < numbers[i]+numbers[i-1]:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            k = i
            while k < n-1:
                k += 1
                if numbers[k-1]+numbers[k] < numbers[k]+numbers[k-1]:
                    numbers[k], numbers[k - 1] = numbers[k - 1], numbers[k]

    answer = ''.join(numbers)
    answer = int(answer)
    return str(answer)



# 타인 풀이
def solution66(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([12, 121]), '12121')
print(solution([21, 212]), '21221')

print(solution([3, 30, 34, 5, 9, 0, 0, 0, 1000]))
#
# print(solution([3, 382, 38, 321, 9, 0, 40, 403]))

print(solution([42, 3, 3, 3, 3, 322, 32, 23]), '4233333232223')
# print(solution([3, 30, 34, 5, 9, 4, 40, 42]))
# print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([10, 101]), "10110")
print(solution([1, 11, 111, 1111]), "1111111111")
