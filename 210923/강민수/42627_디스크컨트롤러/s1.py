inp = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):

    l = len(jobs)
    ans = 0
    jobs = sorted(jobs, key=lambda a: a[1])

    end = 0
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= end:
                end += jobs[i][1]
                ans += end - jobs[i][0]
                jobs.pop(i)

                break
            elif i == len(jobs) - 1:
                end += 1

    return ans // l