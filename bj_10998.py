input_str = input()

def multiply_for_2args(list_integer):
    return list_integer[0] * list_integer[1]

print(multiply_for_2args(list(map(lambda x: int(x), input_str.split()))))
