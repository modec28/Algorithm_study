N = int(input())
account_list = list()
for _ in range(N):
    age, name = map(str, input().split())
    account_list.append([int(age), name])
account_list.sort(key=lambda x: (x[0]))
for account in account_list:
    print("%d %s" % (account[0], account[1]))