def get_self_number(init_number,max_number):
    prev_num = init_number

    result = list()

    while True:
        next_num = prev_num + sum(list(map(lambda x: int(x), list(str(prev_num)))))

        if next_num > max_number:
            break
        else:
            result.append(next_num)
            prev_num = next_num
    return result


total_generated_number = list()

natural_number = list()
for i in range(1,10001):
    total_generated_number += get_self_number(i, 10000)
    natural_number.append(i)

lasted_result = sorted(list(set(natural_number) ^ set(total_generated_number)))

for last in lasted_result:
    print(last)
