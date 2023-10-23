a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

def solution():
    for i in range(n, n+100):
        if a1*i+a2 > c*i:
            return 0
    return 1

print(solution())

