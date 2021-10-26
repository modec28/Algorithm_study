arg_1 = input()
arg_2 = input()

def chop_numeric_value(int_value):
    return list(map(lambda x: int(x), list(str(int_value))))

def multiply_for_2_value(val_1, val_2):
    return int(val_1) * int(val_2)

chopped_value = chop_numeric_value(arg_2)

for i in range(len(chopped_value)-1,-1,-1):
    print(multiply_for_2_value(arg_1,chopped_value[i]))
print(multiply_for_2_value(arg_1,arg_2))
