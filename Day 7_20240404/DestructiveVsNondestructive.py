list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 비파괴적(자료 원본을 변형시키지 않음)
print(list_a + list_b)
print(list_a)

# 파괴적(자료 원본에 영향을 줌), append(), insert(), expend()가 해당됨
print(list_a.extend(list_b))    # None, list를 변형시키는 메서드로, None을 반환한다.
print(list_a)