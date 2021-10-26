N = int(input())
input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

print(min(input_list), max(input_list))
