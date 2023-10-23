X = int(input())
N = int(input())
Y = 0
for products in range(N):
    info = input().split()
    Y += int(info[0]) * int(info[1])

if Y == X:
    print("Yes")
else:
    print("No")
