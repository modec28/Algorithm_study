input_list = list()
for i in range(10):
    input_list.append(int(input())%42)

print(len(list(set(input_list))))
