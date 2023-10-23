import sys
input_str = sys.stdin.readline()
input_list = list(map(lambda x: int(x), input_str.split()))

N = input_list[0]
X = input_list[1]

input_str = sys.stdin.readline()
input_list = list(map(lambda x: int(x), input_str.split()))

result = ""
for i in range(N):
    if input_list[i] < X:
        result = result + str(input_list[i]) + " "

print(result[:-1])
