def get_gcd(a, b):
    div= a%b
    if div == 0:
        return b
    else:
        return get_gcd(b, div)

def get_lcm(a, b):
    return int(a*b/get_gcd(a,b))

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
if b1> b2:
    lcm = get_lcm(b1,b2)
else:
    lcm = get_lcm(b2,b1)
div = int(a1*lcm/b1 + a2*lcm/b2)
gcd = get_gcd(div, lcm)
print("%d %d" % (div//gcd, lcm//gcd))