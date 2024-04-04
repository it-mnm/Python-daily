# 리스트 요소 하나 제거하기 - 인덱스로 제거하기 : del, pop()

list_a = [0, 1, 2, 3, 4, 5]

# 제거 방법(1) : del
del list_a[1]
print("del list_a[1]: ", list_a)

# 범위지정 제거
del list_a[3:5]
print(list_a)

# 제거 방법(2) : pop()
list_a.pop(2)
print("pop(2): ",list_a)


# 리스트 요소 하나 제거하기 - 값으로 제거하기 :remove()
# 중복되는 값이 있으면 가장 먼저 발견되는 값 하나만 삭제함
list_b = [1, 2, 1, 2]
list_b.remove(2)
print("list_b.remove(2): ",list_b)


# 모두 제거하기 : clear()
list_c = [0, 1, 2, 3, 4]
list_c.clear()
print("list_c.clear()): ",list_c)


# 리스트 정렬 : sort()
list_d = [4, 126, 3, 111, 45]
list_d.sort()                       # 오름차순 정렬
print("list_d.sort(): ",list_d)

list_d.sort(reverse = True)         # 내림차순 정렬
print("list_d.sort(reverse = True): ",list_d)


# 리스트 내부에 있는지 확인하기 : in/not in
list_e = [4, 126, 3, 111, 45]

print("3 in list_e : ", 3 in list_e)                  # True
print("99 in list_e : ", 99 in list_e)                 # False

print("3 not in list_e : ", 3 not in list_e)              # False
print("99 not in list_e : ", 99 not in list_e)             # True
