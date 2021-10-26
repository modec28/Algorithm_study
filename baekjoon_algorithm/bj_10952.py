while True:
    try:
        input_str = input()
        input_list = list(map(lambda x: int(x), input_str.split()))

        print(sum(input_list))
    except:
        break
