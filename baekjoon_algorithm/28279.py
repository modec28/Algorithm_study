import sys

from collections import deque


class Functions:
    
    def __init__(self):
        self.Q = deque()
        self.other_func_lut = {
            "3\n": self._front_with_pop,
            "4\n": self._back_with_pop,
            "5\n": self._size,
            "6\n": self._empty,
            "7\n": self._front_without_pop,
            "8\n": self._back_without_pop
        }

    def _front_with_pop(self) -> int:
        if self._size():
            return self.Q.popleft()
        return -1

    def _back_with_pop(self) -> int:
        if self._size():
            return self.Q.pop()
        return -1

    def _size(self) -> int:
        return len(self.Q)

    def _empty(self) -> int:
        if self._size():
            return 0
        return 1

    def _front_without_pop(self):
        if self._size():
            return self.Q[0]
        return -1

    def _back_without_pop(self):
        if self._size():
            return self.Q[-1]
        return -1

    def __call__(self, command: str):
        if command.startswith("1"):
            _, x = command.split()
            self.Q.appendleft(x)
        elif command.startswith("2"):
            _, x = command.split()
            self.Q.append(x)
        else:
            print(self.other_func_lut[command]())


if __name__ == "__main__":
    N = int(input())
    F = Functions()
    for _ in range(N):
        F(sys.stdin.readline())