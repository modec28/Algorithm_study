import sys

N = int(input())
stack = list()
for _ in range(N):
    command = list(map(int, sys.stdin.readline().rstrip().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)