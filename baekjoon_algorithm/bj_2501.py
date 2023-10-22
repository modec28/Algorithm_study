N, K = map(int, input().split())

result = list()
for num in range(1, N+1):
    if N % num ==0:
        result.append(num)
try:
    print(result[K-1])
except:
    print(0)
