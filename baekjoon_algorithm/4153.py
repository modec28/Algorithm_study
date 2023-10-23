while True:
    input_str = input()
    input_list = sorted(list(map(lambda x: int(x), input_str.split())))

    if input_list == [0,0,0]:
        break
    else:
        a = input_list[0]
        b = input_list[1]
        c = input_list[2]

        if a*a + b*b == c*c:
            print("right")
        else:
            print("wrong")
