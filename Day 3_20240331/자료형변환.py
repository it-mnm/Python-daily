# 문자열을 숫자로 바꾸기 : 캐스트
string_a = input("숫자 a 입력> ")
int_a = int(string_a)
string_b = input("숫자 b 입력> ")
int_b = int(string_b)

print("문자열 자료:",string_a + string_b)
print("숫자 자료:",int_a + int_b)

# 숫자를 문자열로 바꾸기
output_a = str(52)
output_b = str(52.123)
print(type(output_a),output_a)
print(type(output_b),output_b)