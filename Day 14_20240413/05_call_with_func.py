# map() 함수와 filter() 함수

# 함수를 선언합니다.
def power(item):
    return item * item

def under_3(item):
    return item < 3

# 변수를 선언합니다.
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다. : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, lits_input_a) : ", output_a)
print("map(power, lits_input_a) : ", list(output_a))
print()

# filter() 함수를 사용합니다 : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트 구성
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, lits_input_a) : ", output_b)
print("filter(under_3, lits_input_a) : ", list(output_b))