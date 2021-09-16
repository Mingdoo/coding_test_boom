

# test4 104.47ms
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1][:len(phone_book[i])] == phone_book[i][:len(phone_book[i-1])]:
            return False

    return answer

# test4 209.27ms
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


# fail 시간초과
def solution3(phone_book):
    answer = True

    for p in phone_book:
        for a in range(1, len(p)):
            temp = p[:a]
            if temp in phone_book and temp != p:
                return False
    return answer



print(solution2(["12","123","1235","567","88"]))
print(solution2(["119", "97674223", "1195524421"]))