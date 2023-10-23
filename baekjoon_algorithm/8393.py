def sigma_sum(int_num):
    result = 0
    for i in range(1,int_num+1):
        result += i
    return result

input_int = int(input())

print(sigma_sum(input_int))
