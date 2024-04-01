# 구의 부피와 겉넓이를 구하는 프로그램


pi = 3.141592
r = float(input("구의 반지름을 입력해주세요:"))
vol = (4/3) * pi * (r**3)
space = 4 * pi * (r**2)

print(f"= 구의 부피는 {vol}입니다.")
print(f"= 구의 겉넓이는 {space}입니다.")
