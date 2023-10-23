import sys
N = int(input())

numeric_list = list()
for i in range(N):
    numeric_list.append(int(sys.stdin.readline()))

sorted_list = sorted(numeric_list)
for i in sorted_list:
    print(i)
