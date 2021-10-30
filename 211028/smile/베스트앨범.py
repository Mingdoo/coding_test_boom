def solution(genres, plays):
    answer = []
    best = {}
    music = {}
    for i in range(len(genres)):
        best[genres[i]] = best.get(genres[i], 0) + plays[i]
        music[genres[i]] = music.get(genres[i], []) + [(plays[i], i)]

    best = sorted(best.items(), reverse=True, key=lambda item: item[1])

    for gen, pl in best:
        if len(music[gen]) == 1:
            answer.append(music[gen][0][1])
        else:
            temp = sorted(music[gen], reverse=True)
            temp2 = []
            if temp[0][0] == temp[1][0] and temp[0][1] > temp[1][1]:
                answer += [temp[1][1], temp[0][1]]
            else:
                answer += [temp[0][1], temp[1][1]]

    return answer