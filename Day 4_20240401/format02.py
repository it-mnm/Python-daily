# format() 함수의 다양한 기능

# 정수를 특정 칸에 출력하기
output_a = "{:d}".format(52)    # [:d]를 사용 -> int 자료형의 정수를 출력하겠다고 지정
output_b = "{:5d}".format(52)   # [:5d]를 사용 -> 5칸을 빈칸으로 잡고 뒤에서부터 52라는 숫차를 채움
output_c = "{:10}".format(52)   # [:10d]를 사용 -> 10칸을 빈칸으로 잡고 뒤에서부터 52라는 숫차를 채움
# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
# 출력
print("# 기본")
print("output_a",output_a)
print("# 특정칸에 출력하기")
print("output_b",output_b)
print("output_c",output_c)
print("# 빈칸을 0으로 채우기")
print("output_d",output_d)
print("output_e",output_e)
