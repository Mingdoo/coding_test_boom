import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0]-x[1])

state = 0

for a in range(len(arr)-1):
    al = arr[a][0] - arr[a][1]
    ar = arr[a][0] + arr[a][1]
    for b in range(a+1, len(arr)):
        bl = arr[b][0] - arr[b][1]
        br = arr[b][0] + arr[b][1]
        if bl > ar:
            break

        if al <= bl <= ar and ar <= br:
            print("NO")
            state = 1
            break

        if bl <= al and al <= br <= ar:
            print("NO")
            state = 1
            break

    if state == 1:
        break

if state != 1:
    print("YES")




