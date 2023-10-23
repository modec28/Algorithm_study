def multiply_same_size_matrix(a,b):
    result = list()
    for row in range(len(a)):
        result_1d = list()
        for col in range(len(a[0])):
            if b[row][col] == 0:
                result_1d.append(0)
            else:
                result_1d.append(a[row][col])
        result.append(result_1d)
    return result

def concate_same_size_matrix(a,b):
    result = list()
    for row in range(len(a)):
        result.append(a[row]+b[row])
    return result

def pattern_print(array):

    num = len(array)
    prev_num = num//3

    if prev_num == 1:
        return multiply_same_size_matrix(array,[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    else:
        result = list()
        for i in range(prev_num):
            result.append(array[prev_num][0:prev_num])

        result = pattern_print(result)

        concat_col = concate_same_size_matrix(result,result)
        result = concate_same_size_matrix(result,concat_col)

        pattern_result = result+ result+result

        result = list()
        for i in range(num):
            temp_result = list()
            for j in range(num):
                if (i>=prev_num and i<prev_num<<1) and (j>=prev_num and j<prev_num<<1):
                    temp_result.append(0)
                else:
                    if pattern_result[i][j] == 1:
                        temp_result.append(1)
                    else:
                        temp_result.append(0)
            result.append(temp_result)



        return result

#np.set_printoptions(threshold=np.inf, linewidth=np.inf)
import time

start_time = time.time()
N = int(input())

star_n = [[1] * N for _ in range(N)]
pattern_result = pattern_print(star_n)

for pattern in pattern_result:
    print(''.join(list(map(lambda x: "*" if x==1 else " ", pattern))))
print(time.time()-start_time)
