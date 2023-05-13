'''
    1이 될때까지
    N이 될때까지 아래 둘중 하나를 반복적으로 선택해 수행한다.
    1. N에서 1을뺸다
    2. N을 K로 나눈다.(K로 나누어떨어질때만 가능)
    최소횟수를 구하라
'''

N, K = map(int, input().split())

# 웬만하면 나누는게 빠르겠지

count = 0
while True:
    if N==1:
        break
    if N%K == 0:
        N = N//K
    else:
        N -= 1
    count+=1
print(count)
