"""
주제: 조건문
작성일: 2017. 09. 20.
작성자: 201732022 이승현
"""

# 사용자로부터 2개의 수를 입력 받아, 큰 수를 출력하라
a1= int(input("수 입력 : "))
a2 = int(input("수 입력 : "))
max = 0
i = 0
if(a1>a2):
    print("큰수 : ",a1)
elif(a1<a2):
    print("큰 수 : ",a2)
else:
    print("두 수가 같음")

