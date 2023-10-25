n = int(input())
member = dict()
for log in range(n):
    name, content = map(str, input().split())
    if content == "enter":
        member[name] = True
    else:
        member.pop(name)
member_list = list(member.keys())
member_list.sort(reverse=True)
for name in member_list:
    print(name)