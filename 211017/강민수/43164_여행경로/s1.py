def solution(tickets):
    answer = []
    table = {}
    for start, end in sorted(tickets, key=lambda a: a[1]):
        if not table.get(start, 0):
            table[start] = []
        if not table.get(end, 0):
            table[end] = []
        table[start].append(end)
    def dfs(start):
        while table[start]:
            end = table[start].pop(0)
            dfs(end)
        if not table[start]:
            answer.append(start)
    dfs('ICN')
    answer.reverse()
    return answer
#{'ATL': ['ICN', 'SFO'], 'ICN': ['ATL', 'SFO'], 'SFO': ['ATL']}
print(solution([["ICN", "AFO"], ["ICN", "ATL"], ["AFO", "ATL"], ["ATL", "ICN"], ["ATL","AFO"]]))