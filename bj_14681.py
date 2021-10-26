arg_1 = input()
arg_2 = input()

def get_quadrant(x,y):
    xy = x*y
    if(xy>0):
        if(x>0):
            return "1"
        else:
            return "3"
    else:
        if(x>0):
            return "4"
        else:
            return "2"

print(get_quadrant(int(arg_1), int(arg_2)))
