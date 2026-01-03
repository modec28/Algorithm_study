import sys

from queue import PriorityQueue


n, m = input().split()
N, M = int(n), int(m)
pqueue = PriorityQueue()
queue = []
voca = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    if not voca.get(word):
        voca[word] = 1
        pqueue.put((-len(word), word))
    else:
        voca[word] += 1
        pqueue.put((-len(word)-voca[word]*100, word))
voca = {}
while not pqueue.empty():
    word = pqueue.get()[1]
    if not voca.get(word):
        voca[word] = 1
        print(word)    
    else:
        voca[word] += 1
