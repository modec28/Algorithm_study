N = int(input())

if N==4 or N==7:
    print(-1)
else:
    if N%5 == 0:
        print(int(N/5))
    elif N%5 == 1:
        print(int((N-6)/5) + 2)
    elif N%5 == 2:
        print(int((N-12)/5) + 4)
    elif N%5 == 3:
        print(int((N-3)/5) + 1)
    else:
        print(int((N-9)/5) + 3)
