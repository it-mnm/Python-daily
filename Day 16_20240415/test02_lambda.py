# 실행결과

# # 홀수만 추출하기
# [1, 3, 5, 7, 9]

# # 3 이상, 7 미만 추출하기
# [3, 4, 5, 6]

# # 제곱해서 50 미만 추출하기
# [1, 2, 3, 4, 5, 6, 7]


numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x : x % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x : 3 <= x < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x : x**2 < 50, numbers)))
print()