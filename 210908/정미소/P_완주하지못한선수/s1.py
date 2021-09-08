def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


def solution2(participant, completion):
    dict = {}

    for i in participant:
        # if i not in completion:
        #     return i
        # else:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for j in completion:
        dict[j] -= 1

    for key, val in dict.items():
        if val != 0:
            return key