# 끝자리로 짝수와 홀수 구분

# 숫자 입력
number = input("정수 입력 > ")

# 마지막 자리 추출
last_char = number[-1]  # 현재는 문자열 상태임

# 숫자로 변환
last_char = int(last_char)

# 짝수 조건
if last_char == 0\
    or last_char == 2\
    or last_char == 4\
    or last_char == 6\
    or last_char == 8:

    print("짝수입니다.")

# 홀수 조건
if last_char == 1\
    or last_char == 3\
    or last_char == 5\
    or last_char == 7\
    or last_char == 9:

    print("홀수입니다.")

