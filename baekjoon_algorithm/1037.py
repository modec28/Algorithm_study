import sys

from typing import List


def solution(N: int, A: List[str]):
    max = 0
    min = 1_000_000
    for a in A:
        num = int(a)
        if max < num:
            max = num
        if min > num:
            min = num
    return min * max

def test_case():
    assert solution(1, ["2"]) == 4
    assert solution(2, ["2", "3"]) == 6
    assert solution(2, ["2", "4"]) == 8
    assert solution(2, ["2", "5"]) == 10
    assert solution(4, ["2", "3", "4", "6"]) == 12
    assert solution(2, ["2", "7"]) == 14
    assert solution(2, ["3", "5"]) == 15
    assert solution(4, ["2", "3", "6", "9"]) == 18
    assert solution(4, ["2", "4", "5", "10"]) == 20
    assert solution(2, ["3", "7"]) == 21
    assert solution(2, ["2", "11"]) == 22
    assert solution(4, ["2", "4", "6", "12"]) == 24
    assert solution(2, ["2", "13"]) == 26
    assert solution(2, ["3", "9"]) == 27
    assert solution(4, ["2", "4", "7", "14"]) == 28
    assert solution(6, ["2", "3", "5", "6", "10", "15"]) == 30
    assert solution(22, ["261", "23", "657", "1679", "219", "48691", "19053", "667", "73", "87", "6003", "2117", "5037", "15111", "207", "3", "9", "6351", "29", "69", "2001", "146073"]) == 438219
    assert solution(6, ["32698", "5", "81745", "2", "10", "16349"]) == 163490

if __name__ == "__main__":
    N = int(input())
    A = sys.stdin.readline().split()

    print(solution(N, A))