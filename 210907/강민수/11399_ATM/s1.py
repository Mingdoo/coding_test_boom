import sys
sys.stdin = open('input.txt')

def summation(arr):
    s = 0
    for i in range(1, len(arr) + 1):
        s += (len(arr) - i + 1) * arr[i-1]
    return s


N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
print(summation(arr))

