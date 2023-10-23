x = list()
y = list()
for i in range(3):
    input_str = input()
    input_list = list(map(lambda x: int(x), input_str.split()))

    x.append(input_list[0])
    y.append(input_list[1])

from collections import Counter



x = list(sorted(dict(Counter(x)).items(), key=lambda m: m[1],reverse=False))[0][0]
y = list(sorted(dict(Counter(y)).items(), key=lambda m: m[1],reverse=False))[0][0]

print(str(x) + " " + str(y))
