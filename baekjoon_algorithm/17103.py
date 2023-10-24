import sys
def is_prime(num):
    if num<2:
        return False
    sqrt_num = int(num ** 0.5)
    for x in range(2, sqrt_num+1):
        if num % x == 0:
            return False
    return True

def sol(T):
    max_val = 1000
    prime_dict = {0:0, 1:0}
    for x in range(2, max_val+1):
        if prime_dict.get(x, "") == "":
            if is_prime(x):
                index = 2
                while True:
                    prime_dict[x*index] = 0
                    index +=1
                    if x*index > 1000000:
                        break
    prime_list = list(prime_dict.keys())
    prime_list = list(set(prime_list)^set([x for x in range(1000001)]))
    prime_list.sort()
    n_list = list()
    for _ in range(T):
        n_list.append(int(sys.stdin.readline().rstrip()))

    for n in n_list:
        n2 = n//2
        count = 0
        for x in prime_list:
            if x >=n2+1:
                break
            if prime_dict.get(x, 1) and prime_dict.get(n-x, 1):
                count +=1
        print(count)

sol(int(sys.stdin.readline().rstrip()))