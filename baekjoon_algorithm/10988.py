def solution(word):

    len_word = len(word)
    if len_word%2 ==0:
        for i in range(len_word//2):
            if not word[i] == word[-(i+1)]:
                return 0
    else:
        for i in range(len_word//2-1):
            if not word[i] == word[-(i+1)]:
                return 0
    return 1
word = input()
print(solution(word))