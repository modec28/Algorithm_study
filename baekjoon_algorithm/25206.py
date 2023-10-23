grade2score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
    "P" : 0.0,
}
score_list = list()
grade_list = list()
pass_score = 0
for _ in range(20):
    name, score, grade = input().split()
    if grade == "P":
        pass_score += float(score)
    score_list.append(float(score))
    grade_list.append(float(score)*grade2score[grade])

print(round(sum(grade_list)/(sum(score_list)-pass_score), 6))