# N은 0보다 크거나 같은 정수

def factorial(n: int):
    if n < 2:
        return 1
    result = 1
    for num in range(n, 0, -1):
        result *= num
    return result

def test():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(10) == 3628800

if __name__ == "__main__":
    N = int(input())
    print(factorial(N))