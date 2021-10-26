input_int = int(input())

input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

max_score = max(input_list)
max_index = input_list.index(max(input_list))

input_list = list(map(lambda x: x/max_score * 100, input_list))

print(sum(input_list)/input_int)
