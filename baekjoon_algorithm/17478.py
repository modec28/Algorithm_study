
"""
    문제
    평소에 질문을 잘 받아주기로 유명한 중앙대학교의 JH 교수님은 학생들로부터 재귀함수가 무엇인지에 대하여 많은 질문을 받아왔다.

    매번 질문을 잘 받아주셨던 JH 교수님이지만 그는 중앙대학교가 자신과 맞는가에 대한 고민을 항상 해왔다.

    중앙대학교와 자신의 길이 맞지 않다고 생각한 JH 교수님은 결국 중앙대학교를 떠나기로 결정하였다.

    떠나기 전까지도 제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.

    JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자.

    입력
    교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

    출력
    출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.
"""

def solution(input_1):
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

    def recall(count):
        if count==int(input_1):
            print("____"*count+'"재귀함수가 뭔가요?"')
            print("____"*count+'"재귀함수는 자기 자신을 호출하는 함수라네"')
            return "____"*count+'라고 답변하였지.'
        else:
            print("____"*count+'"재귀함수가 뭔가요?"')
            print("____"*count+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
            print("____"*count+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
            print("____"*count+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
            print(recall(count+1))
            return "____"*count+'라고 답변하였지.'
    print(recall(0))

        )
if __name__ == '__main__':
    (solution(input()))
