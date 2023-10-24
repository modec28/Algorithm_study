def get_gcd(a, b):
    div= a%b
    if div == 0:
        return b
    else:
        return get_gcd(b, div)

def get_lcm(a, b):
    return int(a*b/get_gcd(a,b))

a, b = map(int, input().split())
if a> b:
    print(get_lcm(a,b))
else:
    print(get_lcm(b,a))