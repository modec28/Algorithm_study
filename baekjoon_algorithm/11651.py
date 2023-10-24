N = int(input())
xy_list = list()
for _ in range(N):
    x, y = map(int, input().split())
    xy_list.append([x,y])

xy_list.sort(key = lambda x: (x[1], x[0]))

for xy in xy_list:
    print("%d %d" %(xy[0], xy[1]))