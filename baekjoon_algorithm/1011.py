import math

T = int(input())

for i in range(T):
    input_str = input()
    input_list = list(map(lambda x: int(x), input_str.split()))

    x = input_list[0] # 1
    y = input_list[1] # 5

    distance = y-x #4
    std_n = int(math.sqrt(distance)) #2
    std_n2 = std_n * std_n #4

    distance_n = distance - std_n2 #4-4 = 0

    if distance_n == 0:
        print(std_n*2-1)
    else:
        if distance_n > std_n: # 0 > 2
            print(std_n*2+1)
        else:
            print(std_n*2)
    
