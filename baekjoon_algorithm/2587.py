val_list = list()
for _ in range(5):
    val_list.append(int(input()))
print(int(sum(val_list)/5))
val_list.sort()
print(val_list[2])