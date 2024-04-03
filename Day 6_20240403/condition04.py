# if 조건문에 else 구문을 추가해서 짝수와 홀수 구분하기

# 입력
number = input("정수 입력 > ")
number = int(number)

# 조건문을 사용
if number % 2 == 0:
    # 조건이 참일 때, 짝수조건
    print("짝수입니다")
else:
    # 조건이 거짓일 때, 홀수조건
    print("홀수입니다")