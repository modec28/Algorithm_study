def get_prime_number(limit):
    prime_num_list = [2,3]

    if limit > 4:
        for i in range(4,limit+1):
            is_prime = True
            for j in prime_num_list:
                if i % j == 0:
                    is_prime = False
                    break
            if(is_prime):
                prime_num_list.append(i)
        return prime_num_list
    else:
        return list(filter(lambda x: x<=limit, [2,3]))

M = int(input())
N = int(input())

prime_list = get_prime_number(N)
ranged_prime_list = list(filter(lambda x: x>=M, prime_list))

if len(ranged_prime_list)==0:
    print(-1)
else:
    print(sum(ranged_prime_list))
    print(min(ranged_prime_list))
