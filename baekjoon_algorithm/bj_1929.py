def get_prime_number(limit):
    import math
    prime_num_list = [2,3]

    sqrt_limit = math.sqrt(limit)

    if limit > 4:
        for i in range(4,limit+1):
            is_prime = True
            for j in prime_num_list:
                if j> sqrt_limit:
                    break
                elif i % j == 0:
                    is_prime = False
                    break
            if(is_prime):
                prime_num_list.append(i)
        return prime_num_list
    else:
        return list(filter(lambda x: x<=limit, [2,3]))


input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

M = input_list[0]
N = input_list[1]

prime_list = get_prime_number(N)
ranged_prime_list = list(filter(lambda x: x>=M, prime_list))

for i in ranged_prime_list:
    print(i)
