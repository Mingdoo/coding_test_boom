from itertools import permutations

def isprime(n):
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(n**(0.5) + 1)):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    res = []
    for i in range(2, len(numbers)+1):
        perms = permutations(numbers, i)
        for perm in perms:
            tmp = ''
            for j in range(len(perm)):
                tmp += perm[j]
            res.append(tmp)
    numbers += res
    numbers = list(set(map(int, (set(numbers)))))
    print(numbers)
    cnt = 0
    for i in range(len(numbers)):
        if isprime(int(numbers[i])):
            cnt += 1
            print(numbers[i])
    return cnt

print(solution('011'))