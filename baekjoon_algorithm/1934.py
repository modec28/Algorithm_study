def get_gcd(a, b):
    div= a%b
    if div == 0:
        return b
    else:
        return get_gcd(b, div)

def get_lcm(a, b):
    return int(a*b/get_gcd(a,b))

T = int(input())
result = list()
for _ in range(T):
    a, b = map(int, input().split())
    if a> b:
        result.append(get_lcm(a,b))
    else:
        result.append(get_lcm(b,a))
for res in result:
    print(res)