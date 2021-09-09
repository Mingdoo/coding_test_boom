def solution(participant, completion):
    participant_sorted = sorted(participant)
    completion_sorted = sorted(completion)

    for idx, value in enumerate(completion_sorted):
        if participant_sorted[idx] != value:
            return participant_sorted[idx]

        # 알파벳 순서로 마지막 사람이 완주를 못했을 수 있으므로
    return participant_sorted[-1]