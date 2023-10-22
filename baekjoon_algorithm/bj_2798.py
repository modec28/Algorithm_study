from itertools import combinations

def solution():
    N, M = map(int, input().split())
    card_list = list(map(int, input().split()))

    max_result = 0
    for a,b,c in list(combinations(card_list, 3)):
        value = a+b+c
        if value > max_result and value<=M:
            max_result = value
        if value == M:
            return value
    return max_result

print(solution())
