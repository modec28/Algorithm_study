import sys
N = int(sys.stdin.readline().rstrip())
data_list = list()
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    stack = list()
    for char in data:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
    if stack:
        data_list.append("NO")
    else:
        data_list.append("YES")
for data in data_list:
    print(data)
