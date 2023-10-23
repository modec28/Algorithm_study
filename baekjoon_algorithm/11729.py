N = int(input())

K = 1+2*(2**(N-1)-1)

if N%2==1:
    print(str(1) + " " + str(3))
else:
    print(str(1) + " " + str(2))
