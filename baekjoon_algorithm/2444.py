N = int(input())

for i in range(N):
    print(" "*(N-(i+1))+"*"*(2*i+1))
for i in range(N):
    print(" "*(i+1)+"*"*(2*(N-(i+1))-1))