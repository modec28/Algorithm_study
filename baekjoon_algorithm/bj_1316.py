from collections import Counter

N = int(input())
count = 0
for j in range(N):

    input_str_list = list(input())

    result = list()
    result.append(input_str_list[0])

    for i in range(1,len(input_str_list)):
        if input_str_list[i] == input_str_list[i-1]:
            pass
        else:
            result.append(input_str_list[i])

    result_dict = dict(Counter(result))
    sorted_result_dict = sorted(result_dict.items(), key=lambda x: x[1],reverse=True)

    if(sorted_result_dict[0][1]>1):
        pass
    else:
        count +=1

print(count)
