N, M = map(int, input().split())
poke_num_dict = dict()
poke_char_dict = dict()
for i in range(1, N+1):
    poke_name = input()
    poke_num_dict[i] = poke_name
    poke_char_dict[poke_name] = i
answer_list = list()
for _ in range(M):
    quiz = input()
    if quiz.isdigit():
        answer_list.append(poke_num_dict[int(quiz)])
    else:
        answer_list.append(poke_char_dict[quiz])
for answer in answer_list:
    print(answer)
