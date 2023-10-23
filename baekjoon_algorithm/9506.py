def get_divisor(num):
    result = list()
    for n in range(1, num):
        if num % n ==0:
            result.append(str(n))
    return result

result = list()
while True:
    N = int(input())
    if N == -1:
        break
    div_list = get_divisor(N)
    if sum(map(int, div_list)) == N:
        result.append(str(N)+" = "+" + ".join(div_list))
    else:
        result.append(str(N)+" is NOT perfect.")

for res in result:
    print(res)