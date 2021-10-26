import sys

test_case_number = int(input())

for i in range(test_case_number):
    input_str = sys.stdin.readline()
    input_list = list(map(lambda x: int(x), input_str.split()))

    print("Case #" + str(i+1)+": "+ str(input_list[0])+" + "+str(input_list[1])+" = "+str(sum(input_list)))
