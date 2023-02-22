import unittest

"""
    오븐시계
    브론즈 4

    적당한 양의 재료 -> 요리 완료시간 계산

    입력 : 요리 시작시간(시,분), 요리 필요시간(분)
    입력 제한 : 시(0<=A<=23), 분(0<=B<=59) 빈칸으로 구분, 분(0<=C<=1000)

    출력 : 요리 완료시간(시,분)
    23시 59분 + 1분 = 0시 0분
"""

def solution(input_1,input_2):
    def split_hour_from_min(min):
        return min//60, min%60
    current_hour, current_min = list(map(lambda x: int(x), input_1.split()))
    need_hour, need_min = split_hour_from_min(int(input_2))
    if current_min + need_min > 59:
        predicted_hour = current_hour + need_hour + 1
        predicted_min = current_min + need_min - 60
    else:
        predicted_hour = current_hour + need_hour
        predicted_min = current_min + need_min
    predicted_hour = predicted_hour-24 if predicted_hour>=24 else predicted_hour
    return str(predicted_hour) + " " + str(predicted_min)


class TestCase(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solution("14 30","20"),"14 50")
    def test_ex2(self):
        self.assertEqual(solution("17 40","80"),"19 0")
    def test_ex3(self):
        self.assertEqual(solution("23 48","25"),"0 13")
    def test_ex4(self):
        self.assertEqual(solution("0 48","0"),"0 48")
    def test_ex5(self):
        self.assertEqual(solution("23 59","1"),"0 0")
    def test_ex6(self):
        self.assertEqual(solution("23 00","1000"),"15 40")
    def test_ex7(self):
        self.assertEqual(solution("0 59","61"),"2 0")
    def test_ex8(self):
        self.assertEqual(solution("23 0","120"),"1 0")
if __name__ == '__main__':
    unittest.main()
