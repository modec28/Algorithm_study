T = int(input())

for i in range(T):
    input_str = input()
    input_list = list(map(lambda x: int(x), input_str.split()))

    H = input_list[0]
    W = input_list[1]
    N = input_list[2]

    quote = N//H
    rem = N%H

    if rem>0:
        quote += 1
        H = rem
    else:
        pass
    if(quote > 9):
        temp_val = str(H) + str(quote)
    else:
        temp_val = str(H) + "0" + str(quote)

    print(temp_val)
