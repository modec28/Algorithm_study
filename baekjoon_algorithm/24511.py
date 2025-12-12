import sys

from collections import deque
from typing import List


class QueueStack:

    def __init__(self, N: int, A: List[str], B: List[str]):
        self.queue_stack_queue = deque()
        for index, _ in enumerate(range(N)):
            if not int(A[index]):
                self.queue_stack_queue.append(B[index])
            
    def __call__(self, C: List[str]):
        output = []
        if len(self.queue_stack_queue) == 0:
            return C
        for c in C:
            output.append(self.queue_stack_queue.pop())
            self.queue_stack_queue.appendleft(c)
        return list(output)
    
def assign_args(submit: bool = True):
    if submit:
        N = int(input())
        A = sys.stdin.readline().split()
        B = sys.stdin.readline().split()
        M = int(input())
        C = sys.stdin.readline().split()
        return N, A, B, M, C
    else:
        import random
        N = 100_000
        A = [str(1) for _ in range(N)]
        B = [str(random.randrange(1,1_000_000_000)) for _ in range(N)]
        M = 100_000
        C = [str(random.randrange(1,1_000_000_000)) for _ in range(M)]
        qs = QueueStack(N=N, A=A, B=B)
        print(" ".join(qs(C)))
        print("1번 테스트 통과")
        A = [str(0) for _ in range(N)]
        qs = QueueStack(N=N, A=A, B=B)
        print(" ".join(qs(C)))
        print("2번 테스트 통과")
        A = [str(random.randrange(0,2)) for _ in range(N)]
        return N, A, B, M, C
    
if __name__ == "__main__":
    N, A, B, M, C = assign_args(submit=True)
    qs = QueueStack(N=N, A=A, B=B)
    print(" ".join(qs(C)))
