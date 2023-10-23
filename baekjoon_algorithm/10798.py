array_list = list()
for _ in range(5):
    array_list.append(list(map(lambda x: x, input())))

col = 0
row = 0
end_row_list = list()
result = ""
while True:
    try:
        if row not in end_row_list:
            result += array_list[row][col]
    except:
        end_row_list.append(row)
        if len(end_row_list) == 5:
            break
    row += 1
    if row == 5:
        row = 0
        col += 1
print(result)