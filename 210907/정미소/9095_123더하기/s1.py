import sys
sys.stdin = open('input.txt')

T = int(input())


def find_plus(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return find_plus(a-1) + find_plus(a-2) + find_plus(a-3)


for tc in range(1, T+1):
    n = int(input())
    result = find_plus(n)
    print(result)