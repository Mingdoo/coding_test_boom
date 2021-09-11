def solution(array, commands):
    array = [0] + array
    answer = []
    for command in commands:
        start = command[0]
        end = command[1]
        target = command[2]

        answer.append(sorted(array[start : end + 1])[target-1])
    return answer


print(solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))