T = int(input())

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


prime_list = get_prime_number(10000)
for i in range(T):
    n = int(input())

    if n == 0:
        break
    else:

        ranged_prime_list = list(filter(lambda x: x<n, prime_list))
        for i in range(n>>1,-1,-1):
            start_index = i
            if start_index in ranged_prime_list:
                break
        start_index = ranged_prime_list.index(start_index)
        for num in range(start_index, -1, -1):
            if n-ranged_prime_list[num] in ranged_prime_list:
                if (ranged_prime_list[num]<<1) > n:
                    print(str(n-ranged_prime_list[num]) + " " + str(ranged_prime_list[num]))
                    break
                else:
                    print(str(ranged_prime_list[num]) + " " + str(n-ranged_prime_list[num]))
                    break
