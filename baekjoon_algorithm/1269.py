An, Bn = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
A_xor_B = A^B
A_B = A & A_xor_B
B_A = B & A_xor_B
print(len(A_B)+len(B_A))