# 이미지 읽어들이고 저장하기

# 모듈을 읽어들입니다.
from urllib import request

# urllib() 함수로 바이너리를 읽습니다.
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb")     # 바이너리 형식으로 씁니다.
file.write(output)
file.close()