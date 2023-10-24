N = int(input())
x_list = list(map(int, input().split()))
sx_list = list(set(x_list))
sx_list.sort()
answer = dict()
for index in range(len(sx_list)):
    answer[sx_list[index]] = str(index)
print(" ".join([answer[x] for x in x_list]))