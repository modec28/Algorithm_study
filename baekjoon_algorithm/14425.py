N, M = map(int, input().split())
S = dict()
for _ in range(N):
    S[input()] = True
count = 0
for _ in range(M):
    if S.get(input(), False):
        count += 1
print(count)