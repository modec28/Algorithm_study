input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

m = input_list[0]
n = input_list[1]

print((m//n))
print(m%n)
