N = int(input())
card_list = list(map(int, input().split()))
card_dict = dict.fromkeys(card_list, True)
M = int(input())
holdem_list = list(map(int, input().split()))
result = list()
for holdem in holdem_list:
    if card_dict.get(holdem, False):
        result.append("1")
    else:
        result.append("0")
print(" ".join(result))

