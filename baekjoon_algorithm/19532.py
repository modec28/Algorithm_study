def sol(ex_input: str):
    a, b, c, d, e, f = map(int, ex_input.split())
    det = a*e - b*d
    x = (e*c - b*f)/det
    y = (a*f - d*c)/det
    print("%d %d" % (x, y))

sol(input())