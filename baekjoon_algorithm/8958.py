input_int = int(input())



def convert_filtered_O_list(input_str_buffer):
    def sigma_sum(int_num):
        result = 0
        for i in range(1,int_num+1):
            result += i
        return result
    filtered_list = list(filter(None,input_str_buffer.replace("X",",").split(",")))

    print(sum(list(map(lambda x : sigma_sum(len(x)), filtered_list))))



for i in range(input_int):
    input_str = input()
    convert_filtered_O_list(input_str)
