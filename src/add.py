num1 = int(input("첫번째 숫자 입력:"))
연산 = input("연산 선택 (+ - * /):") 
num2 = int(input("두번째 숫자 입력:"))

if 연산 == "+":
    print("결과:", num1 + num2)
else:
    print("잘못된 입력입니다")