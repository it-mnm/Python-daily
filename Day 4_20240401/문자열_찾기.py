# 문자열 찾기 : find()와 rfind()

# find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
# rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.

output_a = "안녕안녕하세요".find("안녕")
print(output_a)     # 0

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)     # 2

# 안녕안녕하세요 에서 안녕이 처음 등장하는 자리는 0, 두번째로 등장하는 자리는 2이다.