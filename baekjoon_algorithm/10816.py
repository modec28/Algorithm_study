N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
has_list = list(map(int, input().split()))

card_dict = dict()
for card in card_list:
    if card_dict.get(card, 0):
        card_dict[card] += 1
    else:
        card_dict[card] = 1
answer_list = list()
for x in has_list:
    answer_list.append(str(card_dict.get(x, 0)))
print(" ".join(answer_list))