results = list()
for case in range(int(input())):
    case_str = input()
    results.append(case_str[0]+case_str[-1])

for result in results:
    print(result)
