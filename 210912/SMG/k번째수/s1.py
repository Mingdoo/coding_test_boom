def solution(array, commands):
    answer = []
    array.append(0)
    for i in commands:
        temp = []
        temp = array[i[0]-1:i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])
    return answer