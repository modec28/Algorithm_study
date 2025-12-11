from collections import deque

if __name__ == "__main__":
    N = int(input())
    Q = deque([x for x in range(1, N+1)])
    while True:
        if len(Q) == 1:
            print(Q[0])
            break
        Q.popleft()
        Q.rotate(-1)