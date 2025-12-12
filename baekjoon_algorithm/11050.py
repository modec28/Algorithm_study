n, k= input().split()
N, K = int(n), int(k)

def factorial(x: int):
    y = 1
    for num in range(x, 1, -1):
        y *= num
    return y

def factorial_remain(a: int, b: int):
    c = a - b
    y = 1
    for num in range(a, c, -1):
        y *= num
    return y
print(int(factorial_remain(N, K)/factorial(K)))