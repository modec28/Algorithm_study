input_str = input()

def divide_for_2args(list_integer):
    return list_integer[0] / list_integer[1]

print(divide_for_2args(list(map(lambda x: int(x), input_str.split()))))
