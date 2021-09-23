def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def powerset(numbers, tmp, cnt=0):
    #종료
    if len(numbers) <= 1:
        tmp += numbers[0]
        res.append(tmp)
        return
    #안종료
    else:
        if cnt < len(numbers):
            tmp += numbers[cnt]
            cnt += 1
            powerset(numbers, tmp, cnt)

            tmp = tmp[:-1]
            powerset(numbers, tmp, cnt)

def solution(numbers):
    answer = 0
    numbers = list(numbers)

    return answer

numbers = '123'
numbers = list(numbers)
res = []
powerset(numbers, '')
print(res)