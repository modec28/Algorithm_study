import math
T = int(input())

for i in range(T):
    input_str = input()
    input_list = list(map(lambda x: int(x), input_str.split()))

    x1 = input_list[0]
    y1 = input_list[1]
    r1 = input_list[2]
    x2 = input_list[3]
    y2 = input_list[4]
    r2 = input_list[5]

    distance_turret = math.sqrt((x1-x2)**2 +(y1-y2)**2)

    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if distance_turret > r1+r2:
            print(0)
        elif distance_turret < r1+r2:
            if distance_turret < abs(r1-r2):
                print(0)
            elif distance_turret == abs(r1-r2):
                print(1)
            else:
                print(2)
        else:
            print(1)
