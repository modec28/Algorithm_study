n = int(input())
for _ in range(n):
    word = input()
    array = [word]
    for row in range(1,len(word)-1):
        text = word[row] + " "*(len(word)-2) + word[-1-row]
        array.append(text)
    if len(word) > 1:
        array.append(word[-1:0:-1]+word[0])
    for sorted_word in array:
        print(sorted_word)