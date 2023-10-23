import sys

result = list()
while True:
    content = sys.stdin.readline().rstrip()
    if not content:
        break
    result.append(content)
for _ in result:
    print(_)
