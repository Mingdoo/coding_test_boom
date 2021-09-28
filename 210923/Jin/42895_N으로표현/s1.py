# 나에겐 정말 어려웠던 문제...
def solution(N, number):
    sets = [set() for _ in range(9)]
    for i in range(1, 7):
        sets[i].add(((10 ** i - 1) // 9) * N)
    for i in range(2, 9):
        for j in range(1, i):
            for k in sets[j]:
                for l in sets[i - j]:
                    sets[i].add(k + l)
                    if 0 < k * l < 100000:
                        sets[i].add(k * l)
                    if l < k:
                        sets[i].add(k - l)
                    if not k % l:
                        sets[i].add(k // l)
    for i in range(1, 9):
        if number in sets[i]:
            return i
    return -1