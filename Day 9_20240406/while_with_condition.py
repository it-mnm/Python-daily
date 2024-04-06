# 해당하는 값 모두 제거하기

# remove() 함수는 리수트 내부에서 해당하는 값 하나만 제거할 수 있음

# 변수를 선언
list_test = [1, 2, 1, 2]
value = 2

# list_test 내부에 value가 있다면 반복 -> remove() 함수를 반복해서 사용할 수 있게됨
while value in list_test:
    list_test.remove(value)

# 출력
print(list_test)