N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0]-x[1])

state = 0

for a in arr:
    al = a[0] - a[1]
    ar = a[0] + a[1]
    for b in arr:
        if a != b:
            bl = b[0] - b[1]
            br = b[0] + b[1]
            if al < bl < ar and ar < br:
                print("NO")
                state = 1
                break
            if bl < al and al < br < ar:
                print("NO")
                state = 1
                break
    if state == 1:
        break

if state != 1:
    print("YES")




