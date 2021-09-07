import sys
sys.stdin = open('input.txt')

it = int(sys.stdin.readline())
arr = [0] * 13
def dp_table(arr):
    for i in range(1, len(arr)):
        if i == 1:
            arr[i] = 1
        elif i == 2:
            arr[i] = 2
        elif i == 3:
            arr[i] = 4
        else:
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

dp_table(arr)

for i in range(it):
    num = int(sys.stdin.readline())
    print(arr[num])