input_str = input()

input_list = list(map(lambda x: int(x), input_str.split()))

A = input_list[0]
B = input_list[1]
C = input_list[2]

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
