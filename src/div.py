def div(a, b):
    try:
        # 1. 입력받은 문자열을 숫자로 변환 
        n1 = float(a)
        n2 = float(b)

        # 2. 0으로 나누기 체크
        if n2 == 0:
            return " 0으로 나눌 수 없습니다."

        # 3. 계산 및 소수점 오차 보정 (10자리)
        result = n1 / n2
        return round(result, 10)

    except ValueError:
        # 숫자가 아닌 값이 입력되었을 경우 예외 처리
        return "숫자만 입력 가능합니다."




