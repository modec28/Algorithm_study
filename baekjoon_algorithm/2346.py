from typing import List
from collections import deque


if __name__ == "__main__":
    N = int(input())
    balloon_number_queue = deque([x for x in range(1, N+1)])
    paper_number_list: List[str] = input().split()
    balloon_paper_key_map = dict(zip(balloon_number_queue, paper_number_list))
    answer_list = []

    answer_list.append(str(balloon_number_queue.popleft()))
    paper_number = int(balloon_paper_key_map[1])
    while len(balloon_number_queue):
        if paper_number > 0:
            paper_number -= 1
            for _ in range(paper_number):
                balloon_number_queue.rotate(-1)
        else:
            for _ in range(abs(paper_number)):
                balloon_number_queue.rotate(1)
        pop_ballon_index = balloon_number_queue.popleft()
        answer_list.append(str(pop_ballon_index))
        paper_number = int(balloon_paper_key_map[pop_ballon_index])
    print(" ".join(answer_list))
