def solution(N, number):
    answer = 1

    if N == number:
        return answer

    lst = [[0], [N], [int(str(N)+str(N)), N*N, N+N, N//N, N-N]]

    answer += 1
    if number in lst[answer]:
        return answer

    lst2 = []
    for k in range(2, 9):
        a = str(N) * k
        lst2.append(int(a))

    for idx in range(3, 9):
        temp = []
        for n in range(1, idx//2+1):
            m = idx - n  #idx=3, n=1, m=2 / idx=4, n=1, m=3 idx=4, n=2, m=2
            for x in lst[m]:
                for y in lst[n]:
                    if x in lst2 and y in lst2:
                        temp.append(int(str(y)+str(x)))
                    temp.append(x + y)
                    temp.append(x * y)
                    if x-y >= 0:
                        temp.append(x - y)
                    if y-x >= 0:
                        temp.append(y - x)
                    if y != 0:
                        temp.append(x // y)
                    if x != 0:
                        temp.append(y // x)
        answer += 1
        if number in temp:
            return answer
        lst.append(temp)

    return -1