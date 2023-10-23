import sys
numeric_dict = dict()
for i in range(int(input())):
    input_int = int(sys.stdin.readline())
    try:
        numeric_dict[input_int] += 1
    except:
        numeric_dict[input_int] = 1

for i,j in sorted(numeric_dict.items(), key=lambda x: x[0]):
    for k in range(j):
        print(i)
