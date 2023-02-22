input_str = input().split()
bucket = ["0" for x in range(int(input_str[0]))]
for method in range(int(input_str[1])):
    method_list = input().split()
    for target in range(int(method_list[0])-1, int(method_list[1])):
        bucket[target] = method_list[2]

print(" ".join(bucket))
