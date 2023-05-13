result_value = 0
result_index = ["1", "0"]

num_list = list(map(int, input().split()))
max_value = max(num_list)
max_index = num_list.index(max_value)

result_value = max_value
result_index[1] = str(max_index+1)

for row in range(1, 9):
    num_list = list(map(int, input().split()))
    max_value = max(num_list)
    max_index = num_list.index(max_value)
    if max_value > result_value:
        result_value = max_value
        result_index = [str(row+1), str(max_index+1)]
print(result_value)
print(" ".join(result_index))
