input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

x = input_list[0]
y = input_list[1]
w = input_list[2]
h = input_list[3]

print(min(x,y,h-y,w-x))
