# 리스트에 요소 추가하기

# 리스트 선언
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가하기
list_a.append(4)
list_a.append(5)
print(list_a)

# 리스트 뒤에 한번에 많은 요소 추가하기
list_a.extend([6, 7, 8])
print(list_a)

# 리스트 중간에 요소 추가하기
list_a.insert(0, 10)       # insert(삽입할 위치, 삽입할 값)
print(list_a)
