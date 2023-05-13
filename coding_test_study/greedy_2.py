'''
    숫자가 쓰인 카드가 N X M 형태로 놓여있다.
    첫째줄에 행, 열을 입력한다
    둘째줄부터 카드를 나타낸다
    행 중에 하나를 선택해서 가장 낮은 숫자를 출력해야한다.
    따라서, 가장 높은 결과를 얻을 수 있는 행을 골라 출력하자.
'''

# 그냥 각 행마다 min 해서 가장 높은 값 출력하면될듯

result = list()
N, M = map(int, input().split())
card_min_list = list()
for _ in range(N):
    card_min_list.append(min(list(map(int, input().split()))))
print(max(card_min_list))


