import sys

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


T = int(input())

for _ in range(T):
    N, M = sys.stdin.readline().split()
    print(int(factorial_remain(int(M), int(N))/factorial(int(N))))