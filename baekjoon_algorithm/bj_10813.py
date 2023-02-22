input_str = input().split()
bucket = [str(x) for x in range(1,int(input_str[0])+1)]

for method in range(int(input_str[1])):
    temp = input().split()
    a = int(temp[0])-1
    b = int(temp[1])-1
    if a!=b:
        a_val = bucket[a]
        b_val = bucket[b]

        bucket.pop(b)
        if a-b != -1:
            bucket.pop(a)

        bucket.insert(a,b_val)

        if a-b != -1:
            bucket.insert(b,a_val)
print(" ".join(bucket))
