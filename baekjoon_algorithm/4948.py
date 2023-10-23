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

prime_list = get_prime_number(123456*2)
while True:
    n = int(input())

    if n == 0:
        break
    else:

        ranged_prime_list = list(filter(lambda x: x>n and x<=2*n, prime_list))

        print(len(ranged_prime_list))
