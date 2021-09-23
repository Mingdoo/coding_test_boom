import math

def comp(a, b): # 숫자들 비교하는 함수
    aa = int(math.log10(a)) + 1
    bb = int(math.log10(b)) + 1
    if a * (10 ** bb) + b >= b * (10 ** aa) + a:
        return True
    else:
        return False

lst = list(range(1, 1001))
n = 1000
for i in range(n - 1): # 버블 정렬
    for j in range(n - 1, i, -1):
        if not comp(lst[j - 1], lst[j]):
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
lst.append(0)

def solution(numbers):
    answer = ''
    cnt = {}
    for i in numbers:
        cnt[i] = cnt.get(i, 0) + 1

    for j in lst:
        how_many = cnt.get(j, 0)
        if how_many:
            answer += f'{j}' * how_many
    for idx, value in enumerate(answer):
        if value == '0':
            pass
        else:
            return answer[idx:]

    return '0' # 너무한다...