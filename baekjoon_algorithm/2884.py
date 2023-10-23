input_str = input()

input_list = list(map(lambda x: int(x), input_str.split()))

hour = input_list[0]
min = input_list[1]

if(min<45):
    min = 15 + min
    if(hour == 0):
        hour = 23
    else:
        hour = hour -1
else:
    min = min-45

print(hour, min)
