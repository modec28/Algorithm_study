import sys


class Palindrome:

    def __init__(self):
        self.call_count = 0

    def __enter__(self):
        self.call_count = 0

    def __exit__(self, exc_type, exc_value, traceback):
        self.call_count = 0

    def recursion(self, s, l, r):
        self.call_count += 1
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return self.recursion(s, l+1, r-1)

    def isPalindrome(self, s):
        return self.recursion(s, 0, len(s)-1)
    
    def print(self, result: int):
        print(f"{result} {self.call_count}")

N = int(input())
palindrome = Palindrome()
for _ in range(N):
    text = sys.stdin.readline().rstrip()
    with palindrome:
        result = palindrome.isPalindrome(text)
        palindrome.print(result)
