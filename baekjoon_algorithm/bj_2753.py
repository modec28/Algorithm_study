input_int = int(input())

def is_quot(int_year,quot):
    return (int_year % quot) == 0
def is_not_quot(int_year,quot):
    return (int_year % quot) != 0

if is_quot(input_int,4) and (is_not_quot(input_int,100) or is_quot(input_int,400)):
    print("1")
else:
    print("0")
