const_range_num = 10

arg_1 = input()
arg_2 = input()
arg_3 = input()

multiply_result = int(arg_1) * int(arg_2) * int(arg_3)

#print(multiply_result)

from collections import Counter

result_dict = dict(Counter(list(str(multiply_result))))

sorted_result_dict = sorted(result_dict.items())
key_result_list = list(map(lambda x: int(x[0]),sorted_result_dict))

for i in range(const_range_num):
    if(i in key_result_list):
        print(sorted_result_dict[key_result_list.index(i)][1])
    else:
        print(0)
