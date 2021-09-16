import sys
sys.stdin = open('input.txt')

N = int(input())
P = list(map(int, input().split()))
result = []
total = 0
P.sort()
for i in P:
    if len(result):
        temp = result[-1] + i
        result.append(temp)
    else:
        result.append(i)

print(sum(result))