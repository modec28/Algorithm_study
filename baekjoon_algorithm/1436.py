'''
아래 코드를 돌려봤더니 266800까지 했을때 10,000개까지 찾고, 내 노트북 기준 0.56초 걸림
미리 키밸류 넣고 빼는 방식으로 접근해도될듯
from tqdm import tqdm
import time
start_time = time.time()
count = 0
for i in tqdm(range(2666800)):
    if "666" in str(i):
        count+=1
print(time.time()-start_time)
print(count)
print("End")
'''
answer = dict()
count = 0
for i in range(2666800):
    if "666" in str(i):
        count+=1
        answer[str(count)] = i
print(answer[input()])
        