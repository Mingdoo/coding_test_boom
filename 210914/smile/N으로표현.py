def solution(N, number):
    answer = 0
    lst = [[N]]
    print(lst)
    cnt = 0

    while answer <= 4:
        temp = []
        templ = lst.pop()
        for i in templ:
            temp.append(i * N)
            temp.append(i // N)
            temp.append(i + N)
            temp.append(i - N)
            temp.append(int(str(i) + str(N)))
        lst.append(temp)
        cnt += 1
        print(lst)
        answer += 1
        if number in lst:
            return answer
    print(lst)


print(solution(5, 12))