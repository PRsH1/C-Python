"""
주제:조건문을 이용해 배수,공배수를 판단하고 출력
작성일:2017.9.21.
작성자:이승현
"""
n=int(input("정수를 입력하세요:"))#안내문 출력
if(n%3==0 and n%4==0):#3과 4로 나누어지면
    print("3과 4의 공배수")#결과값 출력
elif n%3==0:#3으로 나누어지면
    print("3의 배수")#결과값 출력
elif n%4==0:#4로 나누어지면
    print("4의 배수")#결과값 출력
else:#아무것도 아니면
    print("3의 배수도, 4의 배수도 아닙니다")#결과값 출력