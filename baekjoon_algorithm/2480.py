import unittest

"""
    문제
    1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

    같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
    같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
    모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
    예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

    3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

    입력
    첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

    출력
    첫째 줄에 게임의 상금을 출력 한다.
"""

def solution(input_1):
    dice_list = list(map(lambda x: int(x), input_1.split()))
    aigen_list = list(set(dice_list))
    if len(dice_list) == len(aigen_list):
        return max(dice_list)*100
    elif len(aigen_list) == 1:
        return 10000+aigen_list[0]*1000
    else:
        print(aigen_list)
        for aigen_value in aigen_list:
            print("before : ",dice_list)
            del dice_list[dice_list.index(aigen_value)]
            print("after : ",dice_list)
        return 1000 + dice_list[0]*100

class TestCase(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solution("3 3 6"),1300)
    def test_ex2(self):
        self.assertEqual(solution("2 2 2"),12000)
    def test_ex3(self):
        self.assertEqual(solution("6 2 5"),600)
    def test_ex4(self):
        self.assertEqual(solution("1 1 1"),11000)
    def test_ex5(self):
        self.assertEqual(solution("1 1 6"),1100)
    def test_ex6(self):
        self.assertEqual(solution("6 1 1"),1100)
    def test_ex7(self):
        self.assertEqual(solution("1 6 1"),1100)
if __name__ == '__main__':
    #print(solution(input()))
    unittest.main()
