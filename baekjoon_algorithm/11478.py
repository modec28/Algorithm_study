S = input()
s_list = list()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s_list.append(S[i:j])
print(len(set(s_list)))