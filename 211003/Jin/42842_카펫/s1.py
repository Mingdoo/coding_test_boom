def solution(brown, yellow):
    x = int((brown + 4 +((brown + 4)**2 - 8*(2 * yellow + 2 * brown))**(1/2)) / 4 )
    y = (brown + yellow) // x
    return [x, y]