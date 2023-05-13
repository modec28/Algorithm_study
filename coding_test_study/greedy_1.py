'''
    큰 수의 법칙
    배열의 크기 N, 숫자가 더해지는 횟수 M, K가 첫째줄에 주어질때
    둘째줄의 배열의 가장 큰 수가 나오는 케이스를 출력하라
'''

N, M, K = input().split()
N, M, K = int(N), int(M), int(K)
array = input().split()

# 제일 큰 수와 두번째로 큰 수만 찾으면 될듯

array_int = list(map(lambda x: int(x), array))
array_int.sort(reverse=True)
first_num = array_int[0]
second_num = array_int[1]

print((M//(K+1))*(K*first_num+second_num)+(M%(K+1)*first_num))
