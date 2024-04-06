# 5초 동안 반복하기

# 시간과 관련된 기능을 가져옵니다.
import time

# 변수 선언
number = 0


# 5초 동안 반복합니다.
# time.time()은 유닉스타임 : 1970년 1월 1일 0시 0분 0초를 기준으로 몇초가 지났는지 정수로 나타낸것
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))