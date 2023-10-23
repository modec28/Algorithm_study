input_int = int(input())

cycle_count = 1

def run_cycle(int_num):
    if int_num < 10:
        post_int = int_num
    else:
        post_int = int(int_num/10) + int_num%10

    return int(str(int_num %10) + str(post_int % 10))

result = run_cycle(input_int)

if(result == input_int):
    print(cycle_count)
else:
    cycle_count += 1

    while True:
        try:
            state_result = run_cycle(result)

            if(state_result == input_int):
                print(cycle_count)
                break
            else:
                cycle_count += 1
                result = state_result
        except Exception as e:
            print(e)
            break
