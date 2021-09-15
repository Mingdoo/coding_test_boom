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