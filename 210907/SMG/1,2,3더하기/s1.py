import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

for i in range(N):
    n_list = [0, 1, 2, 4]
    n = int(sys.stdin.readline())
    if n < len(n_list):
        print(n_list[n - 1])
    else:
        for j in range(len(n_list), n + 1,):
            n_list.append(n_list[j-1] + n_list[j-2] + n_list[j-3])
        print(n_list[n])