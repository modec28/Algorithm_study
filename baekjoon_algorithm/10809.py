input_str = input()

str_buffer = ""
for i in range(97,123):
    try:
        str_buffer += str(input_str.index(chr(i))) + " "
    except:
        str_buffer += "-1 "

print(str_buffer[:-1])
