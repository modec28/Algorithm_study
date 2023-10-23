import sys

test_case_number = int(input())

for i in range(test_case_number):
    input_str = sys.stdin.readline()
    input_list = list(map(lambda x: int(x), input_str.split()))

    print(sum(input_list))
