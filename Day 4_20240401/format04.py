# 조합해보기
output_j = "{:+5d}".format(52)      # 기호를 뒤로 밀기 : 양수
output_k = "{:+5d}".format(-52)     # 기호를 뒤로 밀기 : 음수
output_l = "{:=+5d}".format(52)     # 기호를 앞으로 밀기 : 양수
output_m = "{:=+5d}".format(-52)    # 기호를 앞으로 밀기 : 음수
output_n = "{:+05d}".format(52)     # 0으로 채우기 : 양수
output_o = "{:+05d}".format(-52)    # 0으로 채우기 : 음수

print("# 조합하기")
print("output_j",output_j)
print("output_k",output_k)
print("output_l",output_l)
print("output_m",output_m)
print("output_n",output_n)
print("output_o",output_o)
