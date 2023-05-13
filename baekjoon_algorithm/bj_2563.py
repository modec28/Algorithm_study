def solution(debug=False, n=1, xy_list = list(), answer = 0):
    array = [[0 for x in range(100)] for y in range(100)] 

    if not debug:
        num_paper = int(input())
    else:
        num_paper = n

    for i in range(num_paper):
        if not debug:
            x, y = map(int, input().split())
        else:
            x, y = xy_list[i][0], xy_list[i][1]
        dx = x+10 if x+10<100 else 100
        dy = y+10 if y+10<100 else 100
        for row in range(y-1, dy-1):
            for col in range(x-1, dx-1):
                array[row][col] = 1
    
    assert sum(list(map(lambda x: sum(x), array))) == answer
'''
solution(debug=True, n=2, xy_list=[[3,3], [2,2]], answer=119)
solution(debug=True, n=2, xy_list=[[3,7], [3,7]], answer=100)
solution(debug=True, n=3, xy_list=[[3,7], [3,7], [3,7]], answer=100)
solution(debug=True, n=3, xy_list=[[1,1], [2,1], [3,1]], answer=120)
solution(debug=True, n=3, xy_list=[[3,7], [15,7], [5,2]], answer=260)
'''

array = [[0 for x in range(100)] for y in range(100)] 

num_paper = int(input())

for i in range(num_paper):
    x, y = map(int, input().split())
    
    dx = x+10 if x+10<100 else 100
    dy = y+10 if y+10<100 else 100
    for row in range(y-1, dy-1):
        for col in range(x-1, dx-1):
            array[row][col] = 1

print(sum(list(map(lambda x: sum(x), array))))