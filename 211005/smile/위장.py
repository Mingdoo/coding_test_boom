def solution(clothes):
    cloth_dict = {}

    for i in range(len(clothes)):
        cloth_dict[clothes[i][1]] = cloth_dict.get(clothes[i][1], 0) + 1

    answer = 1
    for i in cloth_dict.values():
        answer *= (i+1)

    return answer - 1



print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))