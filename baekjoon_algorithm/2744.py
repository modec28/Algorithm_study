from collections import deque


def convert(text: str) -> str:
    result = deque(text)
    for _ in range(len(text)):
        char = result.popleft()
        if char == char.lower():
            result.append(char.upper())
        else:
            result.append(char.lower())
    return "".join(result)

if __name__ == "__main__":
    word = input()
    print(convert(word))