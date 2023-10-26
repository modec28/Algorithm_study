import queue
stack = list()
N = int(input())
queue_list = queue.deque(list(map(int, input().split())))
count = 1
for _ in range(N*2):
    if stack and stack[-1] == count:
        count+=1
        stack.pop()
        continue
    if not len(queue_list):
        if not stack:
            break
        continue
    user = queue_list.popleft()
    if user == count:
        count += 1
    else:
        stack.append(user)
if count == N + 1:
    print("Nice")
else:
    print("Sad")



