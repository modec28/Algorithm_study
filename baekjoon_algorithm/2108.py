import sys


class Arithmetric:

    def __init__(self):
        self._pod = []
        self._count = {}
        self._sum = 0

    def __count(self, number: int):
        count = self._count.get(number)
        if count:
            self._count[number] += 1
        else:
            self._count[number] = 1

    @property
    def debug(self):
        return self._pod

    @property
    def mean(self):
        return int(round(self._sum/len(self._pod),0))
    
    @property
    def median(self):
        return self._pod[(len(self._pod)-1)//2]
    
    @property
    def mode(self):
        max_count = 0
        max_number = 0
        candidate = []
        for number, count in self._count.items():
            if count > max_count:
                candidate = [number]
                max_count = count
                max_number = number
            elif count == max_count:
                candidate.append(number)
        if not candidate:
            return max_number
        if len(candidate) == 1:
            return candidate[0]
        candidate.sort()
        return candidate[1]
    
    @property
    def range(self):
        return self._pod[-1] - self._pod[0]
    
    def __binary_insert(self, number: int):
        left_index = 0
        right_index = len(self._pod)-1
        if self._pod[right_index] < number:
            self._pod.append(number)
            return
        if self._pod[left_index] > number:
            self._pod.insert(0, number)
            return
        median_index = (left_index + right_index)//2
        while left_index <= right_index:
            if self._pod[median_index] > number:
                right_index = median_index
            else:
                left_index = median_index
            median_index = median_index = (left_index + right_index)//2
            if left_index == median_index:
                self._pod.insert(left_index+1, number)
                break
    
    def append(self, number: int):
        self._sum += number
        self.__count(number)
        if len(self._pod) > 1:
            # self.__binary_insert(number)
            self._pod.append(number)
        elif len(self._pod) == 0:
            self._pod.append(number)
        else:
            if self._pod[0] > number:
                self._pod.insert(0, number)
            else:
                self._pod.append(number)

    def sort(self):
        self._pod.sort()

    

if __name__ == "__main__":
    import random
    # N = int(input())
    arith = Arithmetric()
    # for _ in range(N):
    # for i in range(500_000):
    #     arith.append(random.randrange(-4000,4001))
        # arith.append(int(sys.stdin.readline()))
    N = int(input())
    arith = Arithmetric()
    for _ in range(N):
        arith.append(int(sys.stdin.readline()))
    arith.sort()
    print(arith.mean)
    print(arith.median)
    print(arith.mode)
    print(arith.range)