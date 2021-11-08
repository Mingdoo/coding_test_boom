def solution(triangle):

    length = len(triangle)

    if len(triangle) == 1:
        return triangle[0]
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]

    for i in range(2, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][i] += triangle[i-1][i-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])


    return max(triangle[-1])



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
