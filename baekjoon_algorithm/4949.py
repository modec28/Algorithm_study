import sys

from collections import deque


class Words:
    SMALL_BRACKET_LEFT = "("
    SMALL_BRACKET_RIGHT = ")"
    BIG_BRACKET_LEFT = "["
    BIG_BRACKET_RIGHT = "]"
    SPACE = " "
    DOT = "."
    END_CONDITION = ".\n"

def check_text(q: deque):
    bracket_stack = []
    for char in q:
        if char == Words.SPACE or char.isalpha() or char == "\n" or char == Words.DOT:
            continue
        elif char == Words.SMALL_BRACKET_RIGHT:
            if not len(bracket_stack) or bracket_stack[-1] != Words.SMALL_BRACKET_LEFT:
                return "no"
            bracket_stack.pop()
        elif char == Words.BIG_BRACKET_RIGHT:
            if not len(bracket_stack) or bracket_stack[-1] != Words.BIG_BRACKET_LEFT:
                return "no"
            bracket_stack.pop()
        elif char == Words.SMALL_BRACKET_LEFT or char == Words.BIG_BRACKET_LEFT:
            bracket_stack.append(char)
        else:
            print(f"엥 예상치 못한상황! <{char}>")
    if len(bracket_stack):
        return "no"
    return "yes"

if __name__ == "__main__":
    text = sys.stdin.readline()
    Q = deque(text)
    while text != Words.END_CONDITION:
        print(check_text(Q))
        text = sys.stdin.readline()
        Q = deque(text)