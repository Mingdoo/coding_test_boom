def findmax(enum):
    tmp = enum[0][1]
    for i in range(len(enum)):
        if enum[i][1] > tmp:
            tmp = enum[i][1]
    return tmp

def solution(priorities, location):
    answer = 0
    priorities = list(enumerate(priorities))
    res = []
    while priorities:
        answer += 1
        v = priorities.pop(0)
        if priorities and findmax(priorities) > v[1]:
            priorities.append(v)
        else:
            res.append(v[0])
            continue
    return res.index(location) + 1

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))