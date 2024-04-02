# 날짜/시간 출력하기

# 날짜와 시간 관련 모듈
import datetime

# 현재 날짜와 시간 구하기
now = datetime.datetime.now()

# 출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
