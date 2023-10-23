def get_hansoo_num(int_num):
    if int_num<100:
        return int_num
    else:
        valid_num = 0
        for i in range(100, int_num+1):
            parsing_list = list(map(lambda x: int(x), list(str(i))))
            if parsing_list[1]-parsing_list[0] == parsing_list[2]-parsing_list[1]:
                valid_num += 1
        return 99+valid_num

input_int = int(input())
print(get_hansoo_num(input_int))
