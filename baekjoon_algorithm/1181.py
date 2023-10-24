N = int(input())
words_list = list()
for _ in range(N):
    words_list.append(input())
words_list = list(set(words_list))
words_list.sort(key=lambda x: (len(x), x))
for word in words_list:
    print(word)