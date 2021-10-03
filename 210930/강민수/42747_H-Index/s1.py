def solution(citations):
    answer = 0
    citations = sorted(citations)
    for i in range(max(citations)):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1
        if i <= cnt:
            answer = i
    return answer