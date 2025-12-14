from typing import List


def check(first: List[str]):
    result = 0
    for num in first:
        result += int(num)**2
    return result%10


if __name__ == "__main__":
    first5 = input().split()
    print(check(first5))