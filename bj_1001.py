input_str = input()

def subtract_for_2args(list_integer):
    return sum([list_integer[0], -list_integer[1]])


print(subtract_for_2args(list(map(lambda x: int(x), input_str.split()))))
