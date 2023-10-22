def solution():

    edge_list = list(map(int, input().split()))

    edge_list.sort()

    if sum(edge_list) == 0:
        return None

    if edge_list[2] >= edge_list[0] + edge_list[1]:
        return "Invalid"

    if edge_list[0] == edge_list[1] and edge_list[1]==edge_list[2] and edge_list[0]==edge_list[2]:
        return "Equilateral"

    if edge_list[0]!=edge_list[1] and edge_list[1]!=edge_list[2] and edge_list[0]!=edge_list[2]:
        return "Scalene"

    return "Isosceles"

result = list()
while True:
    sol = solution()
    if not sol:
        break
    result.append(sol)

for res in result:
    print(res)

