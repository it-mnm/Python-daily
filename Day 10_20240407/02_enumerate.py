# enumerate() 함수와 리스트

# 변수를 선언합니다
example_list = ["요소A", "요소B", "요소C"]

# 그냥 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수 적용
print("# enumerate() 함수 적용")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환해 출력
# (0, '요소A') 같은 것을 튜플이라고 한다.
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))

# for 반복문과 enumerate() 함수 조합해서 사용하기
print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))