def solution(begin, target, words):
    global result, visited, word_lst
    answer = 0
    result = []
    visited = []
    if target not in words:
        return answer

    word_lst = list(set(''.join(words)))
    begin = list(begin)
    n = len(begin)

    for i in range(len(word_lst)):
        for j in range(n):
            tmp = begin[j]
            begin[j] = word_lst[i]
            visited.append(''.join(begin))
            dfs(begin, target, words, 1, n)
            begin[j] = tmp

    return min(result)


def dfs(w, target, words, l, n):
    global result, visited, word_lst

    if ''.join(w) not in words:
        return

    if ''.join(w) == target:
        result.append(l)
        return

    for i in range(len(word_lst)):
        for j in range(n):
            tmp = w[j]
            w[j] = word_lst[i]
            if ''.join(w) not in visited:
                visited.append(''.join(w))
                dfs(w, target, words, l + 1, n)
            w[j] = tmp

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))