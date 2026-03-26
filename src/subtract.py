def subtract(a, b):
    try:
        return(float(a) - float(b))
    except ValueError:
        return "숫자를 입력하십시오."
# 뺄셈 구현