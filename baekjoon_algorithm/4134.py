T = int(input())
answer_list = list()
for _ in range(T):
    n = int(input())
    while True:
        sqrt_n = int(n**0.5)
        is_prime=True
        if n < 9:
            if n in [2,3,5,7]:
                answer_list.append(n)
                break
            else:
                n += 1
                continue
        for x in range(2, sqrt_n+1):
            if n % x == 0:
                n += 1
                is_prime=False
                break
        if is_prime:
            answer_list.append(n)
            break
for answer in answer_list:
    print(answer)
