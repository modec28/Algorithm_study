def solution():
    num_list = list(map(int, input().split()))
    num_list.sort()

    if num_list[2] < num_list[0] + num_list[1]:
        return sum(num_list)

    valid_edge = 0
    for i in range(num_list[0], num_list[2]):
        if i < num_list[0] + num_list[1]:
            valid_edge = i
        else:
            break
    return num_list[0] + num_list[1] + valid_edge

print(solution())