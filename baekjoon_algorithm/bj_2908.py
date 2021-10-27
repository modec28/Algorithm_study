input_str = input()
input_list = list(map(lambda x: x, input_str.split()))

print(max(list(map(lambda x: int(x[::-1]),input_list))))
