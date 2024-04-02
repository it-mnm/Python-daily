# 계절을 구분하는 프로그램

import datetime

now = datetime.datetime.now()

# 봄 구분
if 3 <= now.month <= 5:
    print(f"이번달은 {now.month}월로 봄입니다.")

# 여름 구분
if 6 <= now.month <= 8:
    print(f"이번달은 {now.month}월로 여름입니다.")

# 가을 구분
if 9 <= now.month <= 11:
    print(f"이번달은 {now.month}월로 가을입니다.")

# 겨울 구분
if now.month ==12 or 1<= now.month <= 2:
    print(f"이번달은 {now.month}월로 겨울입니다.")