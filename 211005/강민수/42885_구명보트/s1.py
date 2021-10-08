from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    people = deque(people)
    while people:
        v = people.pop()
        if not people:
            cnt += 1
            break
        if v + people[0] > limit:
            cnt += 1
        else:
            people.popleft()
            cnt += 1
    return cnt

print(solution([100,500,500,900,950], 1000))