import sys
K = int(sys.stdin.readline().rstrip())
answer_list = list()
for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n:
        answer_list.append(n)
    else:
        answer_list.pop()
print(sum(answer_list))