students = [x for x in range(1,31)]
for student in range(28):
    students.pop(students.index(int(input())))
for fallen in students:
    print(fallen)
