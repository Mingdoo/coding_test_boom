# 실패한 풀이,,, 흙

def solution(scoville, k):
    length = len(scoville)
    idx = 0
    residual = []
    answer = 0
    scoville.append(1000000000)
    scoville.sort()
    while idx < length - 1:
        answer += 1
        if residual:
            if residual[0] >= k and scoville[idx] >= k:
                answer -= 1
                return answer
            if residual[0] > scoville[idx + 1]:
                scoville[idx + 1], scoville[idx] = 2 * scoville[idx + 1] + scoville[idx], 0
                if scoville[idx + 1] > scoville[idx + 2]:
                    residual.append(scoville[idx + 1])
                    scoville[idx + 1] = 0
                    idx += 2
                    continue
                else:
                    idx += 1
                    continue

            elif scoville[idx] < residual[0] <= scoville[idx + 1]:
                temp = residual.pop(0)
                scoville[idx] = temp * 2 + scoville[idx]
                if scoville[idx] > scoville[idx + 1]:
                    residual.append(scoville[idx])
                    scoville[idx] = 0
                    idx += 1
                    continue
                else:
                    continue

            else:
                temp = residual.pop(0)
                scoville[idx] = temp + scoville[idx] * 2
                if scoville[idx] > scoville[idx + 1]:
                    residual.append(scoville[idx])
                    scoville[idx] = 0
                    idx += 1
                    continue
                else:
                    continue

        else:
            if scoville[idx] >= k and scoville[idx + 1] >= k:
                answer -= 1
                return answer
            scoville[idx + 1], scoville[idx] = 2 * scoville[idx + 1] + scoville[idx], 0
            if scoville[idx + 1] > scoville[idx + 2]:
                residual.append(scoville[idx + 1])
                scoville[idx + 1] = 0
                idx += 2
                continue
            else:
                idx += 1

    return -1

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))


# def solution(scoville, K):
#     length = len(scoville)
#     idx = 0
#     residual = []
#     answer = 0
#     while idx < length - 1:
#         answer += 1
#         if residual:
#             if residual[0] >= k and scoville[idx] >= k:
#                 answer -= 1
#                 break
#             if residual[0] > scoville[idx + 1]:
#                 scoville[idx + 1], scoville[idx] = 2 * scoville[idx + 1] + scoville[idx], 0
#                 if scoville[idx + 1] > scoville[idx + 2]:
#                     residual.append(scoville[idx + 1])
#                     scoville[idx + 1] = 0
#                     idx += 2
#                     continue
#                 else:
#                     idx += 1
#                     continue
#
#             elif scoville[idx] < residual[0] <= scoville[idx + 1]:
#                 temp = residual.pop(0)
#                 scoville[idx] = temp * 2 + scoville[idx]
#                 if scoville[idx] > scoville[idx + 1]:
#                     residual.append(scoville[idx])
#                     scoville[idx] = 0
#                     idx += 1
#                     continue
#                 else:
#                     continue
#
#             else:
#                 temp = residual.pop(0)
#                 scoville[idx] = temp * 2 + scoville[idx]
#
#             pass
#         else:
#             if scoville[idx] >= k and scoville[idx + 1] >= k:
#                 answer -= 1
#                 break
#             scoville[idx + 1], scoville[idx] = 2 * scoville[idx + 1] + scoville[idx], 0
#             if scoville[idx + 1] > scoville[idx + 2]:
#                 residual.append(scoville[idx + 1])
#                 scoville[idx + 1] = 0
#                 idx += 2
#                 continue
#             else:
#                 idx += 1