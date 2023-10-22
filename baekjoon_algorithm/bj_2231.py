def solution():
    N = int(input())

    if N <= 10:
        delta = N
    else:
        delta = (len(str(N)))*10

    if delta > N:
        delta = N

    for i in range(delta):
        if (N-delta+i) + sum(list(map(lambda x: int(x), str(N-delta+i)))) == N:
            return (N-delta+i)

sol = solution()

if not sol:
    print(0)
else:
    print(sol)