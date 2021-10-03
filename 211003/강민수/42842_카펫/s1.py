def solution(brown, yellow):
    total = brown + yellow
    for i in range(total, 2, -1):
        if total % i == 0:
            width = total // i
            if yellow == (width - 2) * (i - 2):
                return [i, width]