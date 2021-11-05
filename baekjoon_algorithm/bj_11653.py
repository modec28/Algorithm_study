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

N = int(input()) # 12

prime_list = get_prime_number(3200) # 2 3 5 7 11

result = list()
if N in prime_list:
    print(N)
else:
    while True:
        if N==1 :
            break
        is_prime = True
        for prime in prime_list: #
            if N % prime == 0:
                N = N/prime
                result.append(prime)
                is_prime = False
                break
        if(is_prime):
            result.append(int(N))
            break
result = sorted(result)
for i in result:
    print(i)
