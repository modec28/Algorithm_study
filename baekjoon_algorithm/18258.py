import sys

from collections import deque


def push(q: deque, x: int):
    q.append(x)

def pop(q: deque) -> int:
    try:
        return q.popleft()
    except IndexError:
        return -1

def size(q: deque) -> int:
    return len(q)

def empty(q: deque) -> int:
    if size(q):
        return 0
    return 1

def front(q: deque) -> int:
    if size(q):
        return q[0]
    return -1

def back(q: deque) -> int:
    if size(q):
        return q[-1]
    return -1

def call_function(q: deque, function: callable):
    print(function(q))

if __name__ == "__main__":
    N = int(input())
    Q = deque()
    print_funcs: callable = {
        "pop\n": pop,
        "size\n": size,
        "empty\n": empty,
        "front\n": front,
        "back\n": back
    }
    for _ in range(N):
        command = sys.stdin.readline()
        if command.startswith("push"):
            _, x = command.split()
            push(Q, x)
        else:
            call_function(Q, print_funcs[command])