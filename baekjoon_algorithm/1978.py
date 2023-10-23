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

prime_list = get_prime_number(1000)

T = int(input())

input_str = input()
input_list = list(map(lambda x: int(x), input_str.split()))

prime_count = 0
for input_num in input_list:
    if input_num in prime_list:
        prime_count += 1
print(prime_count)
