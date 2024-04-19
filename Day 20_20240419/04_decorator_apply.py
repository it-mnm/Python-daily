# 함수 데코레이터 응용
# https://www.youtube.com/watch?v=03r7sloAyOY

# 양수인지 확인하는 데코레이터
def validate_positive_number(func):
    def wrapper(arg):
        if arg < 0:
            raise ValueError("인자는 0보다 커야합니다.")
        return func(arg)
    return wrapper

# integer인지 확인하는 데코레이터
def validate_integer(func):
    def wrapper(arg):
        if not isinstance(arg, int):
            raise ValueError("인자는 integer여야 합니다.")
        return func(arg)
    return wrapper

@validate_integer
@validate_positive_number
def process_number(num):
    print(f"숫자 검증: {num}")


# 함수 호출
process_number(1.1)