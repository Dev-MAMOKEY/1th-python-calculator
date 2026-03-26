# main.py
# 사칙연산 계산기를 실행하는 메인 프로그램

# 실행법 : src 파일로 이동 후 python main.py 입력

from add import add
from sub import sub
from mul import mul
from div import div

# 반복 실행을 위한 무한 루프
while True:
    # 사용자로부터 첫 번째 숫자, 연산자, 두 번째 숫자 입력받기
    num1 = input("첫번째 숫자 입력: ")
    op = input("연산 선택 (+ - * /): ")
    num2 = input("두번째 숫자 입력: ")

    # 입력한 연산자에 따라 알맞은 함수 호출
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = sub(num1, num2)
    elif op == "*":
        result = mul(num1, num2)
    elif op == "/":
        result = div(num1, num2)
    else:
        result = "잘못된 연산자입니다"

    # 결과 출력
    print("결과:", result)

    # 다시 실행 여부 확인
    again = input("다시 실행하시겠습니까? (y/n): ")

    # y가 아니면 종료
    if again.lower() != "y":
        print("계산기를 종료합니다.")
        break