def func_at(a: int, b: int):
    return (a+b)*(a-b)


if __name__ == "__main__":
    a, b = input().split()
    A, B = int(a), int(b)
    print(func_at(A, B))