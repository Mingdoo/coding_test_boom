import collections

def solution(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    print(a - b)
    print(list(a-b))
    return list(a)[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))