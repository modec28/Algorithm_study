from collections import Counter

input_str = input().upper()

result_dict = dict(Counter(input_str))
sorted_result_dict = sorted(result_dict.items(), key=lambda x: x[1],reverse=True)

if(len(sorted_result_dict)==1):
    print(sorted_result_dict[0][0])
else:
    if(sorted_result_dict[0][1] == sorted_result_dict[1][1]):
        print("?")
    else:
        print(sorted_result_dict[0][0])
