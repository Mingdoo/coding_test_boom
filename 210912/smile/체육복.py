def solution2(n, lost, reserve):
    answer = n
    lost.sort()
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        elif l-1 in range(1, n+1) and l-1 in reserve:
            reserve.remove(l - 1)
        elif l+1 in range(1, n+1) and l + 1 in reserve and l + 1 not in lost:
            reserve.remove(l + 1)
        else:
            answer -= 1

    return answer

def solution3(n, lost, reserve):
    answer = n
    lost.sort()
    for l in lost:
        k = l-1
        j = l+1
        if l in reserve:
            reserve.remove(l)
        elif k in reserve:
            reserve.remove(l - 1)
        elif j in reserve and j not in lost:
            reserve.remove(l + 1)
        else:
            answer -= 1

    return answer



def solution(n, lost, reserve):
    answer = n
    real_lost = []


    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            real_lost.append(l)

    real_lost.sort()

    for lm in real_lost:
        if lm - 1 in range(1, n + 1) and lm - 1 in reserve:
            reserve.remove(lm - 1)
        elif lm + 1 in range(1, n + 1) and lm + 1 in reserve:
            reserve.remove(lm + 1)
        else:
            answer -= 1

    return answer

n = 5
lost = [1, 2, 3]
reserve = [2, 3, 4]
print(solution(n, lost, reserve))