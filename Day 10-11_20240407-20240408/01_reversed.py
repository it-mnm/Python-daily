# reversed() 함수

# 리스트를 선언하고 뒤집습니다.
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

# 출력
print("reversed([1,2,3,4,5]) : ", list_reversed)
print("list(reversed([1,2,3,4,5])) : ", list(list_reversed))

# 반복문 적용
for i in reversed(list_a):
    print("-", i)