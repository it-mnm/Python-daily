# in 문자열 연산자를 활용해서 짝수와 홀수 구분

# 숫자 입력
number = input("정수입력 > ")
last_char = number[-1]

# 짝수 조건
if last_char in "02468":
    print("짝수입니다")

# 홀수 조건
if last_char in "13579":
    print("홀수입니다")
