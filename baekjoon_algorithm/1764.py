N, M = map(int, input().split())

듣도못한사람들 = dict()
for _ in range(N):
    듣도못한사람들[input()] = True
듣도보도못한사람들 = list()
for _ in range(M):
    보도못한사람 = input()
    if 듣도못한사람들.get(보도못한사람, False):
        듣도보도못한사람들.append(보도못한사람)
듣도보도못한사람들.sort()
print(len(듣도보도못한사람들))
for 듣보잡 in 듣도보도못한사람들:
    print(듣보잡)