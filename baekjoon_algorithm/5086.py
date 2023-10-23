def get_type(a,b):
    if a<b:
        if b % a ==0:
            return "factor"
    else:
        if a % b == 0:
            return "multiple"
    return "neither"

result = list()
while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    result.append(get_type(a,b))

for res in result:
    print(res)
    
    