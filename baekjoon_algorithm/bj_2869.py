input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

A = input_list[0]
B = input_list[1]
V = input_list[2]

h = 0
#day = 1
day_climbing = A-B
day = int((V-A)/(A-B))
h = day_climbing*day
day += 1
while True:
    h += A
    if h>=V:
        break
    else:
        h -= B
        day+=1

print(day)
