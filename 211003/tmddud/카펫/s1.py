def solution(brown, yellow):
    aSUMb = (brown + 4)//2
    aMULb = brown + yellow
    for i in range(3, aSUMb//2+2):
        a, b = i, aSUMb - i
        if a*b == aMULb and (a-2)*(b-2) == yellow:
            answer = [b, a]
            return answer
    return 0