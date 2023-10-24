def get_gcd(a, b):
    div = a % b
    if div == 0:
        return b
    else:
        return get_gcd(b, div)

N = int(input())

prev_pos = int(input())
gap_list = list()
for _ in range(N-1):
    pos = int(input())
    gap_list.append(pos-prev_pos)
    prev_pos = pos

gap_list.sort()
gcd = gap_list[0]
for index in range(len(gap_list)-1):
    new_gcd = get_gcd(gcd, gap_list[index+1])
    if gcd > new_gcd:
        gcd = new_gcd
print(sum([(x//gcd)-1 for x in gap_list]))