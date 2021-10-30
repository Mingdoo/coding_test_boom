def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

    n = 2
    while n < len(triangle):
        m = len(triangle[n])
        for i in range(m):
            if i == 0:
                triangle[n][i] += triangle[n - 1][i]
            elif i == m - 1:
                triangle[n][i] += triangle[n - 1][i - 1]
            else:
                triangle[n][i] += max(triangle[n - 1][i], triangle[n - 1][i - 1])
        n += 1

    temp = triangle.pop()

    return max(temp)