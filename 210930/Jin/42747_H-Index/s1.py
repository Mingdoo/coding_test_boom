def solution(citations):
    citations.sort()
    papers = len(citations)
    for i in range(papers - 1, -1, -1):
        if citations[i] < papers - i:
            return papers - i - 1
    return papers