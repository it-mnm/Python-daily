# 계절 구하기

import datetime



# 현재 날짜/시간 구하고 월만 변수에 저장
now = datetime.datetime.now()
month = now.month

# 조건문으로 계절을 확인
if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
else:
    print("겨울")