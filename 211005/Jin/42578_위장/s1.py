def solution(clothes):
    cnt = dict()
    for i in clothes:
        cnt[i[1]] = cnt.get(i[1], 0) + 1
    total = 1
    for value in cnt.values():
        total *= (value + 1)

    return total - 1