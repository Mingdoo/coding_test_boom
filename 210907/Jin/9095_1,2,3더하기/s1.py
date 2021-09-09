lst = [0] + [1, 2, 4] + ([0] * 8)
for n in range(4, 12):
    lst[n] = lst[n-3] + lst[n-2] + lst[n-1]

T = int(input())

for tc in range(1, T + 1):
    target = int(input())
    print(lst[target])