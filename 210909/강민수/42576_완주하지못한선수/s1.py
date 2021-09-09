def solution(participant, completion):
    cnt = {}

    for i in range(len(participant)):
        cnt[participant[i]] = cnt.get(participant[i], 0) + 1

    for j in range(len(completion)):
        cnt[completion[j]] -= 1

    for name, count in cnt.items():
        if count == 1:
            return name

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))