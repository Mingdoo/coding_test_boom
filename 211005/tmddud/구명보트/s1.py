def solution(people, limit):
    boat = 0
    people.sort()
    r = len(people) - 1
    l = 0
    while l < r:
        if people[r] + people[l] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        boat += 1
    if l == r:
        boat += 1
    return boat



people = [70, 50, 80, 50]
limit = 100         # 3
print(solution(people, limit))
people = [40,50,150,160]
limit = 200         # 2
print(solution(people, limit))
people = [100,500,500,900,950]
limit = 1000        # 3
print(solution(people, limit))
