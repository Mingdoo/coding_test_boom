from itertools import permutations

def is_prime(x):
    if x <= 1:
        return 0
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1

def solution(numbers):
    lst = list(numbers)
    answer = 0
    cnt = len(numbers)
    finish = []

    while cnt > 0:
        temp = list(permutations(lst, cnt))
        for i in temp:
            i = ''.join(i)
            if int(i) not in finish:
                if is_prime(int(i)) == 1:
                    finish.append(int(i))
                    answer += 1
        cnt -= 1

    return answer


print(solution("17"), 3)
print(solution(	"011"), 2)