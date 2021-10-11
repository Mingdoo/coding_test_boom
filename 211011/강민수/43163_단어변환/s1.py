def solution(begin, target, words):
    def find_words(begin):
        res = []
        length = len(begin)
        for word in words:
            cnt = 0
            for i in range(length):
                if begin[i] == word[i]:
                    cnt += 1
            if cnt == length - 1:
                res.append(word)
        return res
    visited = dict()
    for word in words:
        visited[word] = visited.get(word, 0)
    stack = [begin]
    visited[begin] = 0
    while stack:
        v = stack.pop()
        for word in find_words(v):
            if visited[word] == 0:
                visited[word] = visited[v] + 1
                stack.append(word)

    answer = visited.get(target, 0)

    return answer

print(solution('hit','cog',['hot','dot','dog','lot','log','cog']))