T = int(input())

for i in range(T):
    input_str = input()
    input_list = list(map(lambda x: x, input_str.split()))

    R = int(input_list[0])
    S = list(input_list[1])

    print(''.join(list(map(lambda x: x*R,S))))
