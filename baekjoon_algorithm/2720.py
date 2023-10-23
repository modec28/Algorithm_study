T = int(input())
Q = 25
D = 10
N = 5
P = 1
result = list()
for _ in range(T):
    C = int(input())
    q = C // Q
    C = C % Q
    d = C // D
    C = C % D
    n = C // N
    C = C % N
    p = C // P
    result.append("%s %s %s %s" %(str(q), str(d), str(n), str(p)))

for res in result:
    print(res)
    
