def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for elem in phone_book[:i] + phone_book[i+1:]:
            if len(phone_book[0]) > len(elem):
                break
            elif len(phone_book[i]) <= len(elem):
                if elem.startswith(phone_book[i]):
                    answer = False
                    return answer
    return answer