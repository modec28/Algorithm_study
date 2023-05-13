N, M = map(int, input().split())

A = list()
for _ in range(N):
    A.append(list(map(int, input().split())))

B = list()
for _ in range(N):
    B.append(list(map(int, input().split())))

for row in range(N):
    print(" ".join([str(A[row][x]+B[row][x]) for x in range(M)]))