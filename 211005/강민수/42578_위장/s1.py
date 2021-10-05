def solution(clothes):
    style = {}
    for cloth in clothes:
        style[cloth[1]] = style.get(cloth[1], 0) + 1

    total = 1
    for num in style.values():
        total *= (num+1)

    return total - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],['a','a'], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))