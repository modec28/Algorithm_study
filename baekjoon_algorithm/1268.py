import sys

num_of_student = int(sys.stdin.readline())
num_of_grade = 5

student_table = list()
for i in range(num_of_student):
    input_str = sys.stdin.readline()
    student_info_list = list(map(lambda x: x, input_str.split()))
    student_table.append(student_info_list)

result = list()
grade_list = list(zip(*student_table))
for i in range(num_of_student):
    temp = list()
    for j in range(num_of_grade):
        temp += list(filter(lambda x: grade_list[j][x] == student_table[i][j], range(len(grade_list[j]))))
    result.append(len(list(set(temp))))
print(result.index(max(result))+1)
