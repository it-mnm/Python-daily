# 나의 정답
list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
output = {}
counter = 0

for i in list:
    if i not in output:
        output[i] = list.count(i)
        counter += 1

print("\n".join(["{}에서",
      "사용된 숫자의 종류는 {}개입니다.",
      "참고: {}"]).format(list, counter, output))


# # 답지
# a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
# counter = {}
# for i in a:
#     if i not in counter:
#         counter[i] = 0
#     counter[i] += 1

# print(f"{a}에서")
# print(f"사용된 숫자의 종류는 {len(counter)}개 입니다.")
# print()
# print(f"참고: {counter}")