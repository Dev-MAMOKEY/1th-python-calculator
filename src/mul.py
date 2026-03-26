# mul.py
# 두 수를 입력받아 곱셈 결과를 반환하는 함수

def mul(a, b):
    try:
        # 입력값을 실수로 변환한 뒤 곱셈 수행
        return round(float(a) * float(b), 3)
    
    except ValueError:
        # 숫자가 아닌 값이 들어오면 오류 메시지 반환
        return "숫자를 입력해야 합니다"