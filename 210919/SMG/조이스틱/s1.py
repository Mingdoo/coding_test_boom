def solution(name):
    answer = 0
    a = '0BCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = '0ZYXWVUTSRQPONMLKJIHGFEDCB'

        for i in name:
            if i == 'A':
                pass
            elif a.index(i) >= b.index(i):
                answer += b.index(i)
            else:
                answer += a.index(i)
            answer += 1
        return answer-1


print(solution("JAN"))