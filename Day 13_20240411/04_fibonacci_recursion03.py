# 재귀함수로 구현한 피보나치 수열(3)

# 변수를 선언합니다.
counter = 0

# 함수를 선언합니다.
def fibonacci(n):
    counter += 1
    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

# 함수를 호출합니다. - 에러발생 : UnboundLocalError
# 파이썬은 함수 외부에 있는 변수를 참조하지 못함 -> global 키워드를 사용해야한다.
print(fibonacci(10))
