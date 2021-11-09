import sys

N = int(input())

result_list = list()
for i in range(N):
    result_list.append(int(sys.stdin.readline()))

sorted_list = sorted(result_list)

for i in sorted_list:
    print(i)
