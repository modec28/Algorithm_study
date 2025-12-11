from collections import deque

if __name__ == "__main__":
    str_n, str_k = input().split()
    N, K = int(str_n), int(str_k)
    Q = deque([x for x in range(1, N+1)])
    dying_list = []
    kill_timer = 1
    while len(Q):
        if K == 1:
            dying_list = [str(x) for x in range(1, N+1)]
            break
        if kill_timer == K:
            dying_list.append(str(Q.popleft()))
            kill_timer = 1
        Q.rotate(-1)
        kill_timer += 1
    dying_str_list = ", ".join(dying_list)
    print(f"<{dying_str_list}>")
