"""
주제: 조건문 연습
작성일: 17. 09. 20.
작성자: 201732022 이승현
"""

"""
사용자로부터 2개의 정수를 입력받는다.
어떤 순서로 두 수가 들어오든 상관없이,
두 수의 차이의 절대값을 출력한다.
"""

a1 = int(input("1번째 정수 입력 : "))
a2 = int(input("2번째 정수 입력 : "))

if(a2>a1):
    print(a2-a1)
else:
    print(a1-a2)
