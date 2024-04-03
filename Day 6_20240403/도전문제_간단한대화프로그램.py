# 간단한 대화 프로그램

import datetime

text = input("입력 > ")
time = datetime.datetime.now().hour

if "안녕" in text:
    print("안녕하세요")
elif "몇 시" in text:
    print(f"지금은 {time}시입니다.")
else:
    print(text)