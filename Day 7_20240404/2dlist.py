# 2차원 리스트에 반복문 두번 사용하여 리스트 전개

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
    for item in items:
        print(item)


# 좀더 알아보기 - 전개 연산자
# * 기호를 통해 리스트를 전개할 수 있다.
# 전개 연산자는 비파괴적으로 동작함 (원본을 변형하지 않음)

# 1. 리스트 내부
a = [1, 2, 3, 4]
b = [*a, *a]
print("[*a, *a] :",b)

# append() 함수를 비파괴적으로 재구현
a.append(5)
print("a.append(5) : ", a)
print("a : ", a)    # 원본이 변형됨

b = [1, 2, 3, 4]
c = [*b, 5]
print("b : ",b)     # 원본 유지
print("c : ",c)


# 2. 함수의 매개변수 위치
print(*a)