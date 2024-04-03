# 나중에 구현하려고 비워 둔 구문

# 입력을 받음
number = input("정수 입력 > ")
number = int(number)

# 조건문 사용
# if 문 아래에 비워놓으면 에러발생
# 0을 넣기에는 다른 개발자들이 오해할 여지가 있음
# 따라서 pass를 사용

if number > 0:
    # 양수일 때 : 미구현상태입니다.
    pass
else:
    # 음수일 때 : 미구현상태입니다.
    pass

# pass 도 미구현 상태를 표현하기엔 부족할 수 있음
# 따라서 raise NotImplementedError 를 사용하여 "아직 구현하지 않은 부분입니다"라는 오류를 강제 발생시킴
if number > 0:
    # 양수일 때 : 미구현상태입니다.
    raise NotImplementedError
else:
    # 음수일 때 : 미구현상태입니다.
    raise NotImplementedError