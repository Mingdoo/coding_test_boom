def solution(numbers, target):
    length = len(numbers)
    bit = 2**length - 1
    answer = 0
    for i in range(bit):
        total = 0
        for j in range(length):
            if 1 << j & i:
                total += numbers[j]
            else:
                total -= numbers[j]
        if total == target:
            answer += 1
    return answer