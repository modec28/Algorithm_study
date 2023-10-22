n = int(input())
'''
1   0
2   0
3   1   1*1
4   4   2*2
5   10  3*3 + 1
6   20  4*4 + 2*2
7   35  5*5 + 3*3 + 1
8   56  6*6 + 4*4 + 2*2
9   84  7*7 + 5*5 + 3*3 + 1
10  120 8*8 + 6*6 + 4*4 + 2*2 + 1
'''
if n<3:
    print(0)
else:
    if n%2 == 0:
        print(sum([x**2 for x in range(2, n-2+1, 2)]))
    else:
        print(sum([x**2 for x in range(1, n-2+1, 2)]))
print(3)