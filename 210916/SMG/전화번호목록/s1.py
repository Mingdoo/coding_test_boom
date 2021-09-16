def solution(phone_book):
    answer = True
    for i in phone_book:
        for j in phone_book:
            if j != i and len(j) <= len(i):
                if i.startswith(j):
                    answer = False
                    return answer
    return answer


def solution(phone_book):
    answer = True
    temp = [0] + [{}] * 20
    for i in phone_book:
        temp[len(i)][i] = 1

    for i in phone_book:
        length = len(i)
        for j in range(1, length):
            if temp[j].get(i[:j], 0):
                return False

    return answer

def solution2(phone_book):
    answer = True
    dict = {}
    for p in phone_book:
        dict[p] = 1

    for p in phone_book:
        for a in range(1, len(p)):
            temp = p[:a]
            if temp in dict and temp != p:
                return False
    return answer