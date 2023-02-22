N = int(input())
I = input().split()
v = input()
count = 0
for i in I:
    if i == v:
        count += 1
print(count)
