input_int = int(input())

for i in range(input_int):
    input_str = input()
    input_list = list(map(lambda x: int(x), input_str.split()))
    input_length = input_list[0]

    avg_float = sum(input_list[1:])/input_length

    cond_length = len(list(filter(None,list(map(lambda x: x if x>avg_float else None, input_list[1:])))))

    print(str("{:.3f}%".format(round(cond_length*100/input_length,3))))
