def gcd(a: str, b: str):
    if a > b:
        bigger, smaller = int(a), int(b)
    else:
        bigger, smaller = int(b), int(a)
    while smaller != 0:
        temp = smaller
        smaller = bigger % smaller
        bigger = temp
    return bigger

def lcm(a: str, b: str):
    return int(a)*int(b) / gcd(a, b)

if __name__ == "__main__":
    p, q, s = input().split()
    if lcm(p, q) <= int(s):
        print("yes")
    else:
        print("no")
