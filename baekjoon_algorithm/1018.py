N, M = map(int, input().split())
answer_row = N-8+1
answer_col = M-8+1
answer = list()
for _ in range(answer_row):
    temp_answer = list()
    for _ in range(answer_col):
        temp_answer.append([0,0])
    answer.append(temp_answer)
ws = "WBWBWBWB"
bs = "BWBWBWBW"
for row in range(N):    
    data = input()
    for ac in range(answer_col):
        for i in range(ac, ac+8):
            for ar in range(answer_row):
                if row >=ar+8 or row < ar:
                    continue
                if row%2 ==0:
                    if (data[i] != ws[i-ac]):
                        answer[ar][ac][0] +=1
                    if (data[i] != bs[i-ac]):
                        answer[ar][ac][1] +=1
                else:
                    if (data[i] != bs[i-ac]):
                        answer[ar][ac][0] +=1
                    if (data[i] != ws[i-ac]):
                        answer[ar][ac][1] +=1
print(min(sum(sum(answer, []),[])))