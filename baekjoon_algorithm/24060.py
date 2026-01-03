from typing import List

class MergeSort:
    def __init__(self, target: int):
        self.target = target
        self.count = 0
        self.target_value = -1

    def merge(self, int_list: List[int], front: int, median: int, rear: int):
        _front, _median = front, median + 1
        temp = []
        while _front <= median and _median <= rear:
            if int_list[_front] <= int_list[_median]:
                temp.append(int_list[_front])
                _front += 1
            else:
                temp.append(int_list[_median])
                _median += 1
        while _front <= median:
            temp.append(int_list[_front])
            _front +=1
        while _median <= rear:
            temp.append(int_list[_median])
            _median +=1
        _front = front
        _temp = 0
        while _front <= rear:
            self.count += 1
            if self.count == self.target:
                self.target_value = temp[_temp]
            int_list[_front] = temp[_temp]
            _front += 1
            _temp += 1

    def merge_sort(self, int_list: List[int], front: int, rear: int):
        if front < rear:
            median = (front + rear)//2
            self.merge_sort(int_list, front, median)
            self.merge_sort(int_list, median+1, rear)
            self.merge(int_list, front, median, rear)
        return int_list
    
    @property
    def print_target(self):
        return self.target_value
        

if __name__ == "__main__":
    import sys

    N, K = map(int, input().split())
    ms = MergeSort(target=K)
    number_list = list(map(int, sys.stdin.readline().rstrip().split()))
    ms.merge_sort(number_list, 0, N-1)
    print(ms.print_target)