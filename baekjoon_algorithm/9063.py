from bisect import bisect_left, bisect_right

N = int(input())
x_list = list()
y_list = list()

def adjust_array(_list, _z):
    if bisect_left(_list, _z) == 0:
        _list.pop(0)
        _list.insert(0, _z)
    elif bisect_right(_list, _z) == 2:
        _list.pop()
        _list.append(_z)
    return _list

for _ in range(N):
    x, y = map(int, input().split())
    if len(x_list)<2:
        x_list.append(x)
        y_list.append(y)
        x_list.sort()
        y_list.sort()
    else:
        x_list = adjust_array(x_list, x)
        y_list = adjust_array(y_list, y)

if len(x_list)<2:
    print(0)
else:
    print((x_list[1] - x_list[0])*(y_list[1] - y_list[0]))