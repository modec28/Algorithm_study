input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))
fixed_cost = input_list[0]
variable_cost = input_list[1]
price = input_list[2]
sales = 1

if price > variable_cost:
    print(int(1+fixed_cost/(price-variable_cost)))
else:
    print("-1")
