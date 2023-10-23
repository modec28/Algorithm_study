input_str = input().split()
N = int(input_str[0])
M = int(input_str[1])
bucket = [str(x) for x in range(1,N+1)]
for x in range(M):
    temp = input().split()
    a = int(temp[0])-1
    b = int(temp[1])-1
    temp = bucket.copy()
    for i in range(b-a+1):
        temp[a+i] = bucket[b-i]
    bucket = temp

print(" ".join(bucket))
