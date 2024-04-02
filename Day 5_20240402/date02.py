# 오전과 오후를 구분하는 프로그램

import datetime

now = datetime.datetime.now()

# 오전 구분
if now.hour < 12:
    print(f"현재시각은 {now.hour}시로 오전입니다.")

if now.hour > 12:
    print(f"현재시각은 {now.hour}시로 오후입니다.")